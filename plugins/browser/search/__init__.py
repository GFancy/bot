from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand

from .data_source import get_search

# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字
@on_command('search', aliases=('搜索', '百度'))
async def search(session: CommandSession):
        text = session.get('text', prompt='你想查询什么呢？')
    search_report = await get_search(text)
    await session.send(search_report)


# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@search.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['text'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的信息不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg


# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'搜索'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'search')
