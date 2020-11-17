from models import Tag


async def fill_tags():
    for tag in ['AI', 'BigData', 'BlockChain']:
        if not await Tag.get_or_none(name=tag):
            await Tag.create(name=tag)
