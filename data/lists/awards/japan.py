#!/usr/local/bin/env python
# -*- coding: utf-8 -*-


d = {
    'competition': 'J. League Division 1',
    'team_data': ['Champion'],

    'Champion': [
        ('1993', 'Verdy Kawasaki'),
        ('1994', 'Verdy Kawasaki'),
        ('1995', 'Yokohama Marionos'),
        ('1996', 'Kashima Antlers'),
        ('1997', 'Jubilo Iwata'),
        ('1998', 'Kashima Antlers'),
        ('1999', 'Jubilo Iwata'),
        ('2000', 'Kashima Antlers'),
        ('2001', 'Kashima Antlers'),
        ('2002', 'Jubilo Iwata'),
        ('2003', 'Yokohama F. Marinos'),
        ('2004', 'Yokohama F. Marinos'),
        ('2005', 'Gamba Osaka'),
        ('2006', 'Urawa Red Diamonds'),
        ('2007', 'Kashima Antlers'),
        ('2008', 'Kashima Antlers'),
        ('2009', 'Kashima Antlers'),
        ('2010', 'Nagoya Gramus Eight'),
        ('2011', 'Kashiwa Reysol'),
        ('2012', 'Sanfrecce Hiroshima'),
    ],

    'MVP':  [
        ('1993', 'Kazuyoshi Miura'),
        ('1994', 'Pereira'),
        ('1995', 'Dragan Stojković'),
        ('1996', 'Jorginho'),
        ('1997', 'Dunga Júbilo'),
        ('1998', 'Masashi Nakayama'),
        ('1999', 'Alessandro Santos'),
        ('2000', 'Shunsuke Nakamura'),
        ('2001', 'Toshiya Fujita'),
        ('2002', 'Naohiro Takahara'),
        ('2003', 'Emerson'),
        ('2004', 'Yuji Nakazawa'),
        ('2005', 'Araújo'),
        ('2006', 'Marcus Tulio'),
        ('2007', 'Robson Ponte'),
        ('2008', 'Marquinhos'),
        ('2009', 'Mitsuo Ogasawara'),
        ('2010', 'Seigo Narazaki'),
        ('2011', 'Leandro Domingues'),
        ('2012', 'Hisato Sato'),
        ],

    'Rookie of the Year': [
        ('1993', 'Masaaki Sawanobori'),
        ('1994', 'Kazuaki Tasaka'),
        ('1995', 'Yoshikatsu Kawaguchi'),
        ('1996', 'Toshihide Saito'),
        ('1997', 'Atsushi Yanagisawa'),
        ('1998', 'Shinji Ono'),
        ('1999', 'Yuji Nakazawa'),
        ('2000', 'Kazuyuki Morisaki'),
        ('2001', 'Koji Yamase'),
        ('2002', 'Keisuke Tsuboi'),
        ('2003', 'Daisuke Nasu'),
        ('2004', 'Takayuki Morimoto'),
        ('2005', 'Robert Cullen'),
        ('2006', 'Jungo Fujimoto'),
        ('2007', 'Takanori Sugeno'),
        ('2008', 'Yoshizumi Ogawa'),
        ('2009', 'Kazuma Watanabe'),
        ('2010', 'Takashi'),
        ('2011', 'Hiroki Sakai'),
        ('2012', 'Gaku Shibasaki'),
        ],

    'Manager of the Year': [
        ('1993', 'Yasutaro Matsuki'),
        ('1994', 'Yasutaro Matsuki'),
        ('1995', 'Arsène Wenger'),
        ('1996', 'Nicanor Kashiwa'),
        ('1997', 'João Carlos'),
        ('1998', 'Osvaldo Ardiles'),
        ('1999', 'Steve Perryman'),
        ('2000', 'Akira Nishino'),
        ('2001', 'Masakazu Suzuki'),
        ('2002', 'Masakazu Suzuki'),
        ('2003', 'Takeshi Okada'),
        ('2004', 'Takeshi Okada'),
        ('2005', 'Akira Nishino'),
        ('2006', 'Guido Buchwald'),
        ('2007', 'Oswaldo de Oliveira'),
        ('2008', 'Oswaldo de Oliveira'),
        ('2009', 'Oswaldo de Oliveira'),
        ('2010', 'Dragan Stojković'),
        ('2011', 'Nelsinho Baptista'),
        ('2012', 'Hajime Moriyasu'),
        ],
}

#Best XI

best_xi = {
    1993: [
        'Shigetatsu Matsunaga',
        'Shunzo Ono',
        'Tetsuji Hashiratani',
        'Pereira',
        'Masami Ihara',
        'Takumi Horiike',
        'Santos',
        'Yasuto Honda',
        'Ruy Ramos',
        'Kazuyoshi Miura',
        'Ramón Díaz',
        ],
    
    1994: [
        'Shinkichi Kikuchi',
        'Pereira',
        'Masami Ihara',
        'Yoshihiro Natsuka',
        'Tetsuji Hashiratani',
        'Tsuyoshi Kitazawa',
        'Ruy Ramos',
        'Bismarck',
        'Betinho',
        'Nobuhiro Takeda',
        'Takuya Takagi',
        ],
    
    1995: [
        'Shinkichi Kikuchi',
        'Naoki Soma',
        'Masami Ihara',
        'Masaharu Suzuki',
        'Guido Buchwald',
        'Tetsuji Hashiratani',
        'Bismarck',
        'Masahiro Fukuda',
        'Kazuyoshi Miura',
        'Dragan Stojković',
        'Hiroaki Morishima',
        ],
    
    1996: [
        'Seigo Narazaki',
        'Naoki Soma',
        'Masami Ihara',
        'Guido Buchwald',
        'Jorginho',
        'Masakiyo Maezono',
        'Motohiro Yamaguchi',
        'Hiroshi Nanami',
        'Kazuyoshi Miura',
        'Dragan Stojković',
        'Masayuki Okano',
        ],
    
    1997: [
        'Tomoaki Ogami',
        'Naoki Soma',
        'Masami Ihara',
        'Yutaka Akita',
        'Bismarck',
        'Hidetoshi Nakata',
        'Motohiro Yamaguchi',
        'Hiroshi Nanami',
        'Dunga',
        'Masashi Nakayama',
        'Patrick Mboma',
        ],
    
    1998: [
        'Seigo Narazaki',
        'Naoki Soma',
        'Makoto Tanaka',
        'Yutaka Akita',
        'Shinji Ono',
        'Daisuke Oku',
        'Toshiya Fujita',
        'Hiroshi Nanami',
        'Dunga',
        'Masashi Nakayama',
        'Atsushi Yanagisawa',
        ],
    
    1999: [
        'Masanori Sanada',
        'Yuji Nakazawa',
        'Toshihide Saito',
        'Ryuzo Morioka',
        'Shunsuke Nakamura',
        'Alessandro Santos',
        'Teruyoshi Ito',
        'Masaaki Sawanobori',
        'Takashi Fukunishi',
        'Dragan Stojković',
        'Hwang Sun-Hong',
        ],
    
    2000: [
        'Daijiro Takakuwa',
        'Naoki Matsuda',
        'Yutaka Akita',
        'Hong Myung-Bo',
        'Tomokazu Myojin',
        'Shunsuke Nakamura',
        'Junichi Inamoto',
        'Hiroaki Morishima',
        'Tuto',
        'Masashi Nakayama',
        'Akinori Nishizawa',
        ],
    
    2001: [
        'Arno Van Zwam',
        'Go Oiwa',
        'Yutaka Akita',
        'Akira Narahashi',
        'Mitsuo Ogasawara',
        'Takashi Fukunishi',
        'Toshiya Fujita',
        'Toshihiro Hattori',
        'Koji Nakata',
        'Will',
        'Atsushi Yanagisawa',
        ],
    
    2002: [
        'Hitoshi Sogahata',
        'Hideto Suzuki',
        'Makoto Tanaka',
        'Naoki Matsuda',
        'Mitsuo Ogasawara',
        'Takashi Fukunishi',
        'Toshiya Fujita',
        'Hiroshi Nanami',
        'Emerson',
        'Naohiro Takahara',
        'Masashi Nakayama',
        ],
    
    2003: [
        'Seigo Narazaki',
        'Keisuke Tsuboi',
        'Dutra',
        'Yuji Nakazawa',
        'Mitsuo Ogasawara',
        'Takashi Fukunishi',
        'Daisuke Oku',
        'Yasuhito Endo',
        'Emerson',
        'Ueslei',
        'Tatsuhiko Kubo',
        ],
    
    2004: [
        'Yoichi Doi',
        'Marcus Tulio',
        'Dutra',
        'Yuji Nakazawa',
        'Mitsuo Ogasawara',
        'Makoto Hasebe',
        'Daisuke Oku',
        'Yasuhito Endo',
        'Emerson',
        'Marques',
        'Masashi Oguro',
        ],
    
    2005: [
        'Motohiro Yoshida',
        'Ilian Stoyanov',
        'Marcus Tulio Tanaka',
        'Yuji Nakazawa',
        'Mitsuo Ogasawara',
        'Yuki Abe',
        'Fernandinho',
        'Yasuhito Endo',
        'Tatsuya Furuhashi',
        'Araújo',
        'Hisato Satō',
        ],
    
    2006: [
        'Yoshikatsu Kawaguchi',
        'Marcus Tulio Tanaka',
        'Satoshi Yamaguchi',
        'Akira Kaji',
        'Keita Suzuki',
        'Yuki Abe',
        'Kengo Nakamura',
        'Hiroyuki Taniguchi',
        'Yasuhito Endo',
        'Washington',
        'Magno Alves',
        ],
    
    2007: [
        'Ryōta Tsuzuki',
        'Daiki Iwamasa',
        'Marcus Tulio Tanaka',
        'Satoshi Yamaguchi',
        'Yuki Abe',
        'Keita Suzuki',
        'Robson Ponte',
        'Kengo Nakamura',
        'Yasuhito Endo',
        'Juninho',
        'Baré',
        ],
    
    2008: [
        'Seigo Narazaki',
        'Daiki Iwamasa',
        'Atsuto Uchida',
        'Marcus Tulio Tanaka',
        'Yuji Nakazawa',
        'Satoshi Yamaguchi',
        'Kengo Nakamura',
        'Yoshizumi Ogawa',
        'Yasuhito Endo',
        'Marquinhos',
        'Atsushi Yanagisawa',
        ],
    
    2009: [
        'Eiji Kawashima',
        'Daiki Iwamasa',
        'Atsuto Uchida',
        'Marcus Tulio Tanaka',
        'Yuto Nagatomo',
        'Naohiro Ishikawa',
        'Kengo Nakamura',
        'Mitsuo Ogasawara',
        'Yasuhito Endo',
        'Ryoichi Maeda',
        'Shinji Okazaki',
        ],
    
    
    2010: [
        'Seigo Narazaki',
        'Marcus Tulio Tanaka',
        'Takahiro Masukawa',
        'Tomoaki Makino',
        'Danilson Córdoba',
        'Marcio Richardes',
        'Kengo Nakamura',
        'Jungo Fujimoto',
        'Yasuhito Endo',
        'Ryoichi Maeda',
        'Joshua Kennedy',
        ]
    }
