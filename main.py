from collections import OrderedDict
import json
import logging
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from api.upload.s3 import s3r
from api.translater.trans import translate
from api.chatbot.qna import localQna

from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# LLM 및 임베딩 모델을 저장할 전역 변수
llm_model = None
embedding_model = None

converter = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "https://capstone-dun-two.vercel.app",
]

converter.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

converter.include_router(s3r)
converter.include_router(translate)
converter.include_router(localQna)

class summItem(BaseModel):
    url: str


if __name__ == "__main__":
    uvicorn.run(converter, host="0.0.0.0", port=2000)