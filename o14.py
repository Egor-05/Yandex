from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75BBFD', snow_color='#FFFAFA',
            trunk_color='#A45A52', needls_color='#01796F', sun_color='#FFDB00'):
    im = Image.new('RGB', (width, height))
    dr = ImageDraw.Draw(im)

    dr.rectangle(((0, 0), (width, int(height * 0.8))), sky_color)

    dr.ellipse(((int(0.8 * width), -int(0.2 * height)),
                (int(1.2 * width), int(0.2 * height))),
               sun_color)

    dr.rectangle(((0, int(height * 0.8)), (width, height)),
                 snow_color)

    dr.rectangle(((int(width * 0.45), int(height * 0.9)),
                 (int(width * 0.55), int(height * 0.7))),
                 trunk_color)

    dr.polygon(((int(width * 0.3), int(height * 0.7)),
                (int(width * 0.4), int(height * 0.5)),
                (int(width * 0.35), int(height * 0.5)),
                (int(width * 0.45), int(height * 0.3)),
                (int(width * 0.4), int(height * 0.3)),
                (int(width * 0.5), int(height * 0.1)),
                (int(width * 0.6), int(height * 0.3)),
                (int(width * 0.55), int(height * 0.3)),
                (int(width * 0.65), int(height * 0.5)),
                (int(width * 0.6), int(height * 0.5)),
                (int(width * 0.7), int(height * 0.7)),
                (int(width * 0.3), int(height * 0.7))),
               needls_color)
    im.save(file_name, 'BMP')
