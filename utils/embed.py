import interactions



def create_embed(
        title: str = "",
        description: str = "",
        fields: list[tuple[str, str, bool]] = [],
        color: int = 0x0000FF,
        footer_text: str = None,
        footer_image: str = None,
        include_thumbnail: bool = False,
        image: str = None,
        video: str = None,
        thumbnail: str = None,
        include_author: bool = False,
        author_url: str = None,
        author_icon_url: str = None,
        author_name: str = None
) -> interactions.Embed:
    embed = interactions.Embed(
        title=title,
        description=description,
        color=color
    )
    if image:
        embed.set_image(url=image)
    if video:
        embed.set_video(url=video)
    if include_thumbnail:
        embed.set_thumbnail(url=thumbnail)
    if include_author:
        embed.set_author(name=author_name, url=author_url, icon_url=author_icon_url)
    if footer_text:
        embed.set_footer(text=footer_text,
                         icon_url=footer_image if footer_image else "https://cdn.discordapp.com/avatars/1062488482926305300/5ff17afe3c3e2bebd2cf264158b9d720.webp?size=128")
    for field in fields:
        embed.add_field(name=field[0], value=field[1], inline=field[2])
    return embed



def create_error_embed(text: str) -> interactions.Embed:
    return create_embed(
        description=text,
        color=0xFF0000
    )


def create_info_embed(text: str) -> interactions.Embed:
    return create_embed(
        description=text,
        color=0x787774
    )