# -*- coding: utf-8 -*-
from .kakaotalk import parse_pc_kakaotalk, attr
import pandas as pd


def analysis_pc(file):
    title, df = parse_pc_kakaotalk(file)
    df['length'] = df['text'].apply(len)
    df['attr'] = df['text'].apply(attr)
    df = df.astype(dtype={'attr': 'category'})

    # text length
    text = df.groupby(['user', 'attr'])['length'].sum().xs(('text'), level=1).to_dict()
    picture = df.groupby(['user', 'attr'])['length'].count().xs(('picture'), level=1).to_dict()


    return text, picture


if __name__ == '__main__':
    text, picture = analysis_pc('../../../talk/KakaoTalk_20210416_0303_32_121_group_하태유니맹.txt')
    print(text, picture)