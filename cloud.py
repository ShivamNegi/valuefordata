from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

YOUR_TEXT = "something something something is hei afsdhif afhsd"

tags = make_tags(get_tag_counts(YOUR_TEXT), maxsize=120)

create_tag_image(tags, 'cloud_large.png', size=(900, 600), fontname='Lobster')

rankmyskills@gmail.com
