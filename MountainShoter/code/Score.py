#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import os


class Score:
    FILE_PATH = "pontuacao.json"

    @staticmethod
    def save(name: str, score: int):
        scores = Score.get_all()
        scores.append({"name": name, "score": score})

        scores = sorted(scores, key=lambda k: k['score'], reverse=True)[:7]

        with open(Score.FILE_PATH, 'w') as f:
            json.dump(scores, f)

    @staticmethod
    def get_all():
        if not os.path.exists(Score.FILE_PATH):
            return []
        try:
            with open(Score.FILE_PATH, 'r') as f:
                return json.load(f)
        except:
            return []