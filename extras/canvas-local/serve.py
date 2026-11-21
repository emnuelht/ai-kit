#!/usr/bin/env python3
"""Servidor local do canvas (só biblioteca padrão). Escuta apenas em 127.0.0.1.
- serve .ai/design/canvas/
- GET  /__version   muda quando qualquer arquivo do canvas muda (o navegador recarrega sozinho)
- GET/POST /__feedback   comentários e decisões → .ai/design/canvas/feedback.json (o Claude lê)
- POST /__save      salva edições de texto feitas no canvas (só dentro de screens/)
Uso: python .ai/design/canvas-local/serve.py [--port 4317] [--open]
"""
import http.server, json, os, socketserver, sys, threading, webbrowser

ROOT = os.path.dirname(os.path.abspath(__file__))
SCREENS = os.path.join(ROOT, "screens")
FEEDBACK = os.path.join(ROOT, "feedback.json")
PORT = int(sys.argv[sys.argv.index("--port") + 1]) if "--port" in sys.argv else 4317

def version():
    h = 0
    for d, _, files in os.walk(ROOT):
        for f in files:
            if f == "feedback.json":
                continue
            try:
                st = os.stat(os.path.join(d, f)); h ^= hash((f, st.st_mtime_ns, st.st_size))
            except OSError:
                pass
    return str(h)

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=ROOT, **k)

    def log_message(self, *a):
        pass

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _json(self, code, obj):
        body = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n > 5_000_000:
            raise ValueError("payload grande demais")
        return json.loads(self.rfile.read(n) or b"{}")

    def _same_origin(self):
        o = self.headers.get("Origin")
        return o is None or o in (f"http://127.0.0.1:{PORT}", f"http://localhost:{PORT}")

    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/":
            self.send_response(302); self.send_header("Location", "/canvas.html"); self.end_headers(); return
        if p == "/__version":
            fb = os.stat(FEEDBACK).st_mtime_ns if os.path.isfile(FEEDBACK) else 0
            return self._json(200, {"version": version(), "feedback": str(fb)})
        if p == "/__feedback":
            if os.path.isfile(FEEDBACK):
                with open(FEEDBACK, encoding="utf-8") as f:
                    return self._json(200, json.load(f))
            return self._json(200, {"comments": [], "status": {}})
        return super().do_GET()

    def do_POST(self):
        if not self._same_origin():
            return self._json(403, {"erro": "origem não permitida"})
        p = self.path.split("?")[0]
        try:
            data = self._body()
        except Exception as e:
            return self._json(400, {"erro": str(e)})
        if p == "/__feedback":
            with open(FEEDBACK, "w", encoding="utf-8") as f:
                json.dump({"comments": data.get("comments", []), "status": data.get("status", {})}, f, ensure_ascii=False, indent=2)
            return self._json(200, {"ok": True})
        if p == "/__save":
            rel = str(data.get("file", "")).lstrip("/").replace("\\", "/")
            target = os.path.realpath(os.path.join(ROOT, rel))
            if not (target.startswith(os.path.realpath(SCREENS) + os.sep) and target.endswith(".html")):
                return self._json(403, {"erro": "só arquivos .html dentro de screens/"})
            with open(target, "w", encoding="utf-8") as f:
                f.write(str(data.get("html", "")))
            return self._json(200, {"ok": True})
        return self._json(404, {"erro": "rota desconhecida"})

class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

if __name__ == "__main__":
    url = f"http://127.0.0.1:{PORT}/canvas.html"
    try:
        srv = Server(("127.0.0.1", PORT), H)
    except OSError:
        print(f"Canvas já está rodando (ou porta ocupada): {url}")
        if "--open" in sys.argv:
            webbrowser.open(url)
        sys.exit(0)
    print(f"Canvas no ar: {url}  (Ctrl+C para parar)", flush=True)
    if "--open" in sys.argv:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    srv.serve_forever()
