from aiohttp import web
from qr_app import middleware, Config
from importlib import import_module
from pathlib import Path
from aiohttp.web_middlewares import normalize_path_middleware
from os import path



class QrApp:
    routes = web.RouteTableDef()

    def __init__(self, routes_path: str = 'qr_app.routes'):
        self._app = web.Application()

        # Adding middlewares
        self._app.middlewares.append(middleware.error_handler)
        self._app.middlewares.append(normalize_path_middleware(append_slash=True))

        # Recursively importing all route modules
        for module_path in Path(routes_path.replace('.', '/')).rglob('*.py'):
            module_name = '.'.join(module_path.parent.parts + (module_path.stem,))
            import_module(module_name)

        # Mounting static files
        static_path = path.join(path.dirname(__file__), 'static')
        self._app.router.add_static('/static/', path=static_path, name='static')

        self._app.add_routes(self.routes)


    def run(self):
        """Run the application."""
        web.run_app(self._app, host=Config.APP_HOST, port=Config.APP_PORT)
    

