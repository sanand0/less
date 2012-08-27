#!/usr/bin/env python

'''
    Colour themes from Microsoft Office 2007.

    Sample usage:
        @import "color_themes.less";            // Include this library

        .theme { .apex; }                       // Define a theme

        a           { .theme[@accent_1];  }     // Use variables in the theme
        a:visited   { .theme[@accent_1b]; }     // ...

    The library defines the following colour variables:
        light_1, dark_1         Basic light and dark colours (white & black)
        light_2, dark_2         Muted light and dark colours
        accent_1 .. accent_6    Theme-specific colours

    To increase the lightness or darkness, add the following suffixes:
        _l10:  Brighter by 10%
        _l20:  Brighter by 20%
              ...
        _l90:  Brighter by 90%
        _d10:  Darker  by 10%
        _d20:  Darker  by 20%
              ...
        _d90:  Darker  by 90%

    For example,
        accent_1_b30 is 30% brighter than accent_1
        light_2_d20  is 20% darker   than light_2
'''

import colorsys

themes = [
  ['office'     , '#ffffff', '#000000', '#eeece1', '#1f497d', '#4f81bd', '#c0504d', '#9bbb59', '#8064a2', '#4bacc6', '#f79646', ],
  ['apex'       , '#ffffff', '#000000', '#c9c2d1', '#69676d', '#ceb966', '#9cb084', '#6bb1c9', '#6585cf', '#7e6bc9', '#a379bb', ],
  ['aspect'     , '#ffffff', '#000000', '#e3ded1', '#323232', '#f07f09', '#9f2936', '#1b587c', '#4e8542', '#604878', '#c19859', ],
  ['civic'      , '#ffffff', '#000000', '#c5d1d7', '#646b86', '#d16349', '#ccb400', '#8cadae', '#8c7b70', '#8fb08c', '#d19049', ],
  ['concourse'  , '#ffffff', '#000000', '#def5fa', '#464646', '#2da2bf', '#da1f28', '#eb641b', '#39639d', '#474b78', '#7d3c4a', ],
  ['equity'     , '#ffffff', '#000000', '#e9e5dc', '#696464', '#d34817', '#9b2d1f', '#a28e6a', '#956251', '#918485', '#855d5d', ],
  ['flow'       , '#ffffff', '#000000', '#dbf5f9', '#04617b', '#0f6fc6', '#009dd9', '#0bd0d9', '#10cf9b', '#7cca62', '#a5c249', ],
  ['foundry'    , '#ffffff', '#000000', '#eaebde', '#676a55', '#72a376', '#b0ccb0', '#a8cdd7', '#c0beaf', '#cec597', '#e8b7b7', ],
  ['median'     , '#ffffff', '#000000', '#ebddc3', '#775f55', '#94b6d2', '#dd8047', '#a5ab81', '#d8b25c', '#7ba79d', '#968c8c', ],
  ['metro'      , '#ffffff', '#000000', '#d6ecff', '#4e5b6f', '#7fd13b', '#ea157a', '#feb80a', '#00addc', '#738ac8', '#1ab39f', ],
  ['module'     , '#ffffff', '#000000', '#d4d4d6', '#5a6378', '#f0ad00', '#60b5cc', '#e66c7d', '#6bb76d', '#e88651', '#c64847', ],
  ['opulent'    , '#ffffff', '#000000', '#f4e7ed', '#b13f9a', '#b83d68', '#ac66bb', '#de6c36', '#f9b639', '#cf6da4', '#fa8d3d', ],
  ['oriel'      , '#ffffff', '#000000', '#fff39d', '#575f6d', '#fe8637', '#7598d9', '#b32c16', '#f5cd2d', '#aebad5', '#777c84', ],
  ['origin'     , '#ffffff', '#000000', '#dde9ec', '#464653', '#727ca3', '#9fb8cd', '#d2da7a', '#fada7a', '#b88472', '#8e736a', ],
  ['paper'      , '#ffffff', '#000000', '#fefac9', '#444d26', '#a5b592', '#f3a447', '#e7bc29', '#d092a7', '#9c85c0', '#809ec2', ],
  ['solstice'   , '#ffffff', '#000000', '#e7dec9', '#4f271c', '#4f271c', '#feb80a', '#e7bc29', '#84aa33', '#964305', '#475a8d', ],
  ['technic'    , '#ffffff', '#000000', '#d4d2d0', '#3b3b3b', '#6ea0b0', '#6ea0b0', '#8d89a4', '#748560', '#9e9273', '#7e848d', ],
  ['trek'       , '#ffffff', '#000000', '#fbeec9', '#4e3b30', '#f0a22e', '#a5644e', '#b58b80', '#c3986d', '#a19574', '#c17529', ],
  ['urban'      , '#ffffff', '#000000', '#dedede', '#424456', '#53548a', '#438086', '#a04da3', '#c4652d', '#8b5d3d', '#5c92b5', ],
  ['verve'      , '#ffffff', '#000000', '#d2d2d2', '#666666', '#ff388c', '#e40059', '#9c007f', '#68007f', '#005bd3', '#00349e', ],
]

print '/*' + __doc__ + '*/'

M = 255.0
for theme in themes:
    print '.%s { ' % theme[0]


    for i, color in enumerate('light_1 dark_1 light_2 dark_2 accent_1 accent_2 accent_3 accent_4 accent_5 accent_6'.split(' ')):
        c = theme[i+1]
        r, g, b = int(c[1:3],16)/M, int(c[3:5],16)/M, int(c[5:7],16)/M
        h, l, s = colorsys.rgb_to_hls(r, g, b)
        print '  %s@%s: %s;' % (' '*(8-len(color)), color, c),
        for j in range(10,100,10):
            r, g, b = colorsys.hls_to_rgb(h, l*(100-j)/100, s)
            print '%s@%s_d%d: #%02x%02x%02x;' % (' '*(8-len(color)), color, j,
                int(r*255+0.5), int(g*255+0.5), int(b*255+0.5)),
        for j in range(10,100,10):
            r, g, b = colorsys.hls_to_rgb(h, l+(1-l)*j/100, s)
            print '%s@%s_b%d: #%02x%02x%02x;' % (' '*(8-len(color)), color, j,
                int(r*255+0.5), int(g*255+0.5), int(b*255+0.5)),
        print ''

    print '}\n'

