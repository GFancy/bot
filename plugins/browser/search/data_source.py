import plugins.browser.search.Baidu

async def get_search(text: str) -> str:
    # 这里简单返回一个字符串

    mess = f'{text}的搜索结果\n'
    #mess = mess + '   1'
    mess = mess + plugins.browser.search.Baidu.getfromBaidu(text,1)
    return mess
