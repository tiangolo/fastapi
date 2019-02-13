"""FastAPI framework, high performance, easy to learn, fast to code, ready for production"""

__version__ = "0.3.0"

from .applications import FastAPI
from .routing import APIRouter
from .params import Body, Path, Query, Header, Cookie, Form, File, Security, Depends
