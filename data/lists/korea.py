#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

mvp = [
    (1983, 'Park Seong-Hwa'),
    (1984, 'Park Chang-Seon'),
    (1985, 'Han Moon-Bae'),
    (1986, 'Lee Heung-Sil'),
    (1987, 'Chung Hae-Won'),
    (1988, 'Park Kyung-Hoon'),
    (1989, 'Noh Soo-Jin'),
    (1990, 'Choi Jin-Han'),
    (1991, 'Chung Yong-Hwan'),
    (1992, 'Hong Myung-Bo'),
    (1993, 'Lee Sang-Yoon'),
    (1994, 'Ko Jeong-Woon'),
    (1995, 'Shin Tae-Yong'),
    (1996, 'Kim Hyun-Seok'),
    (1997, 'Kim Joo-Sung'),
    (1998, 'Ko Jong-Soo'),
    (1999, 'Ahn Jung-Hwan'),
    (2000, 'Choi Yong-Soo'),
    (2001, 'Shin Tae-Yong'),
    (2002, 'Kim Dae-Eui'),
    (2003, 'Kim Do-Hoon'),
    (2004, 'Nadson'),
    (2005, 'Lee Chun-Soo'),
    (2006, 'Kim Do-Heon'),
    (2007, 'Tavares'),
    (2008, 'Lee Woon-Jae'),
    (2009, 'Lee Dong-Gook'),
    (2010, 'Kim Eun-Jung'),
    ]

rookie = [
    (1985, 'Lee Heung-Sil'),
    (1986, 'Ham Hyun-Gi'),
    (1987, 'Kim Joo-Sung'),
    (1988, 'Hwangbo Kwan'),
    (1989, 'Ko Jeong-Woon'),
    (1990, 'Song Ju-Seok'),
    (1991, 'Jo Woo-Seok'),
    (1992, 'Shin Tae-Yong'),
    (1993, 'Jeong Kwang-Seok'),
    (1994, 'Choi Yong-Soo'),
    (1995, 'Roh Sang-Rae'),
    (1996, 'Park Kun-Ha'),
    (1997, 'Shin Jin-Won'),
    (1998, 'Lee Dong-Gook'),
    (1999, 'Lee Sung-Jae'),
    (2000, 'Yang Hyun-Jung'),
    (2001, 'Song Chong-Gug'),
    (2002, 'Lee Chun-Soo'),
    (2003, 'Jung Jo-Gook'),
    (2004, 'Moon Min-Kwi'),
    (2005, 'Park Chu-Young'),
    (2006, 'Yeom Ki-Hun'),
    (2007, 'Ha Tae-Goon'),
    (2008, 'Lee Seung-Yeoul'),
    (2009, 'Kim Young-Hoo'),
    (2010, 'Yoon Bit-Garam'),
]

best_xi = {
    1983: [ 
        ('South Korea', 'Cho Byung-Deuk', 'Hallelujah'),
        ('South Korea', 'Park Seong-Hwa', 'Hallelujah'),
        ('South Korea', 'Kim Cheol-Su', 'POSCO'),
        ('South Korea', 'Chang Woe-Ryong', 'Daewoo'),
        ('South Korea', 'Lee Kang-Jo', 'Yukong'), 
        ('South Korea', 'Cho Kwang-Rae', 'Daewoo'),
        ('South Korea', 'Park Chang-Sun', 'Hallelujah'), 
        ('South Korea', 'Park Yoon-Gi', 'Yukong'),
        ('South Korea', 'Lee Gil-Yong', 'POSCO'),
        ('South Korea', 'Lee Chun-Seok', 'Daewoo'),
        ('South Korea', 'Kim Yong-Se', 'Yukong'),
        ],
    1984: [  
        ('South Korea', 'Oh Yeon-Kyo', 'Yukong'), 
        ('South Korea', 'Chung Yong-Hwan', 'Daewoo'),
        ('South Korea', 'Park Kyung-Hoon', 'POSCO'),
        ('South Korea', 'Park Seong-Hwa', 'Hallelujah'),
        ('South Korea', 'Jung Jong-Soo', 'Yukong'), 
        ('South Korea', 'Park Chang-Sun', 'Hallelujah'),
        ('South Korea', 'Huh Jung-Moo', 'Hyundai'),
        ('South Korea', 'Cho Young-Jeung', 'Lucky-Goldstar'), 
        ('South Korea', 'Choi Soon-Ho', 'POSCO'),
        ('South Korea', 'Lee Tae-Ho', 'Daewoo'),
        ('South Korea', 'Baek Jong-Chul', 'Hyundai'),
        ],
    1985: [ 
        ('South Korea', 'Kim Hyun-Tae', 'Lucky-Goldstar'), 
        ('South Korea', 'Chang Woe-Ryong', 'Daewoo'),
        ('South Korea', 'Han Moon-Bae', 'Lucky-Goldstar'),
        ('South Korea', 'Choi Kang-Hee', 'Hyundai'),
        ('South Korea', 'Kim Chul-Soo', 'POSCO'), 
        ('South Korea', 'Park Sang-In', 'Hallelujah'),
        ('South Korea', 'Lee Heung-Sil', 'POSCO Atoms'),
        ('South Korea', 'Park Hang-Seo', 'Lucky-Goldstar'), 
        ('South Korea', 'Kim Yong-Se', 'Yukong'),
        ('Thailand', 'Piyapong Pue-on', 'Lucky-Goldstar'),
        ('South Korea', 'Kang Deuk-Soo', 'Lucky-Goldstar'),
        ],
    1986: [  
        ('South Korea', 'Kim Hyun-Tae', 'Lucky-Goldstar'), 
        ('South Korea', 'Cho Young-Jeung', 'Lucky-Goldstar'),
        ('South Korea', 'Kim Pyung-Seok', 'Hyundai'),
        ('South Korea', 'Choi Kang-Hee', 'Hyundai'),
        ('South Korea', 'Park No-Bong', 'Daewoo'), 
        ('South Korea', 'Cho Min-Kuk', 'Lucky-Goldstar'),
        ('South Korea', 'Lee Heung-Sil', 'POSCO'),
        ('South Korea', 'Yoon Sung-Hyo', 'Hanil Bank'), 
        ('South Korea', 'Kim Yong-Se', 'Yukong'),
        ('South Korea', 'Chung Hae-Won', 'Daewoo'),
        ('South Korea', 'Ham Hyun-Gi', 'Hyundai'),
        ],
    1987: [  
        ('South Korea', 'Kim Poong-Joo', 'Daewoo'), 
        ('South Korea', 'Gu Sang-Bum', 'Lucky-Goldstar'),
        ('South Korea', 'Choi Ki-Bong', 'Yukong'),
        ('South Korea', 'Chung Yong-Hwan', 'Daewoo'),
        ('South Korea', 'Park Kyung-Hoon', 'POSCO'), 
        ('South Korea', 'Kim Sam-Soo', 'Hyundai'),
        ('South Korea', 'Noh Soo-Jin', 'Yukong'),
        ('South Korea', 'Lee Heung-Sil', 'POSCO'), 
        ('South Korea', 'Choi Sang-Kook', 'POSCO'),
        ('South Korea', 'Chung Hae-Won', 'Daewoo'),
        ('South Korea', 'Kim Joo-Sung', 'Daewoo'),
        ],
    1988: [  
        ('South Korea', 'Oh Yeon-Kyo', 'Hyundai'), 
        ('South Korea', 'Choi Kang-Hee', 'Hyundai'),
        ('South Korea', 'Choi Tae-Jin', 'Daewoo'),
        ('South Korea', 'Son Hyung-Sun', 'Daewoo'),
        ('South Korea', 'Kang Tae-Sik', 'POSCO'), 
        ('South Korea', 'Choi Jin-Han', 'Lucky-Goldstar'),
        ('South Korea', 'Kim Sang-Ho', 'POSCO'),
        ('South Korea', 'Hwangbo Kwan', 'Yukong'), 
        ('South Korea', 'Lee Kee-Keun', 'POSCO'),
        ('South Korea', 'Ham Hyun-Gi', 'Hyundai'),
        ('South Korea', 'Shin Dong-Chul', 'Yukong'),
        ],
    1989: [  
        ('South Korea', 'Cha Sang-Kwang', 'Lucky-Goldstar'), 
        ('South Korea', 'Lim Jong-Hun', 'Ilhwa Chunma'),
        ('South Korea', 'Cho Yoon-Hwan', 'Yukong'),
        ('South Korea', 'Choi Yun-Gyeom', 'Yukong'),
        ('South Korea', 'Lee Young-Ik', 'Lucky-Goldstar'), 
        ('South Korea', 'Lee Heung-Sil', 'Pohang'),
        ('South Korea', 'Cho Duck-Jae', 'Daewoo'),
        ('South Korea', 'Kang Jae-Soon', 'Hyundai'), 
        ('South Korea', 'Yoon Sang-Chul', 'Lucky-Goldstar'),
        ('South Korea', 'Cho Geung-Yeon', 'POSCO'),
        ('South Korea', 'Noh Soo-Jin', 'Yukong'),
        ],
    1990: [  
        ('South Korea', 'Yoo Dae-Soon', 'Yukong'), 
        ('South Korea', 'Lim Jong-Hun', 'Ilhwa Chunma'),
        ('South Korea', 'Choi Young-Joon', 'Lucky-Goldstar'),
        ('South Korea', 'Choi Tae-Jin', 'Lucky-Goldstar'),
        ('South Korea', 'Lee Jae-Hee', 'Daewoo'), 
        ('South Korea', 'Choi Jin-Han', 'Lucky-Goldstar'),
        ('South Korea', 'Lee Heung-Sil', 'Pohang'),
        ('South Korea', 'Choi Dae-Shik', 'Lucky-Goldstar'), 
        ('South Korea', 'Yoon Sang-Chul', 'Lucky-Goldstar'),
        ('South Korea', 'Lee Tae-Ho', 'Daewoo'),
        ('South Korea', 'Song Ju-Seok', 'Hyundai'),
        ],
    1991: [  
        ('South Korea', 'Kim Poong-Joo', 'Daewoo'), 
        ('South Korea', 'Chung Yong-Hwan', 'Daewoo'),
        ('South Korea', 'Park Hyun-Yong', 'Daewoo'),
        ('Poland', 'Tadeusz Swiatek', 'Yukong'), 
        ('South Korea', 'Kim Hyun-Seok', 'Hyundai'),
        ('South Korea', 'Lee Young-Jin', 'LG'),
        ('South Korea', 'Kim Joo-Sung', 'Daewoo'),
        ('South Korea', 'Choi Kang-Hee', 'Hyundai'),
        ('South Korea', 'Lee Sang-Yoon', 'Ilhwa'), 
        ('South Korea', 'Lee Kee-Keun', 'POSCO'),
        ('South Korea', 'Ko Jeong-Woon', 'Ilhwa'),
        ],
    1992: [  
        ('Tajikistan', 'Valeri Sarychev', 'Ilhwa'), 
        ('South Korea', 'Hong Myung-Bo', 'POSCO'),
        ('South Korea', 'Lee Jong-Hwa', 'Ilhwa'),
        ('South Korea', 'Park Jung-Bae', 'LG'), 
        ('South Korea', 'Shin Hong-Gi', 'Hyundai'),
        ('South Korea', 'Kim Hyun-Seok', 'Hyundai'),
        ('South Korea', 'Shin Tae-Yong', 'Ilhwa'),
        ('South Korea', 'Park Tae-Ha', 'POSCO'),
        ('South Korea', 'Shin Dong-Chul', 'Yukong'), 
        ('South Korea', 'Park Chang-Hyun', 'POSCO'),
        ('South Korea', 'Lim Keun-Jae', 'LG'),
        ],
    1993: [  
        ('Tajikistan', 'Valeri Sarychev', 'Ilhwa'), 
        ('South Korea', 'Choi Young-Il', 'Hyundai'),
        ('South Korea', 'Lee Jong-Hwa', 'Ilhwa'),
        ('South Korea', 'Yoo Dong-Kwan', 'POSCO'), 
        ('South Korea', 'Kim Pan-Keun', 'Daewoo'),
        ('South Korea', 'Shin Tae-Yong', 'Ilhwa'),
        ('South Korea', 'Kim Dong-Hae', 'LG'),
        ('South Korea', 'Lee Sang-Yoon', 'Ilhwa'),
        ('South Korea', 'Kim Bong-Kil', 'Yukong'), 
        ('South Korea', 'Cha Sang-Hae', 'POSCO'),
        ('South Korea', 'Yoon Sang-Chul', 'LG'),
        ],
    1994: [  
        ('Tajikistan', 'Valeri Sarychev', 'Ilhwa'), 
        ('South Korea', 'Ahn Ik-Soo', 'Ilhwa'),
        ('South Korea', 'Yoo Sang-Chul', 'Hyundai'),
        ('South Korea', 'Hong Myung-Bo', 'POSCO'),
        ('South Korea', 'Huh Ki-Tae', 'Yukong'), 
        ('South Korea', 'Shin Tae-Yong', 'Ilhwa'),
        ('South Korea', 'Ko Jeong-Woon', 'Ilhwa'),
        ('South Korea', 'Hwangbo Kwan', 'Yukong'), 
        ('South Korea', 'Yoon Sang-Chul', 'LG'),
        ('Federal Republic of Yugoslavia', 'Rade Bogdanović', 'POSCO'),
        ('South Korea', 'Kim Kyung-Rae', 'Buffalo'),
        ],
    1995: [  
        ('Tajikistan', 'Valeri Sarychev', 'Ilhwa'), 
        ('South Korea', 'Choi Young-Il', 'Hyundai'),
        ('South Korea', 'Hong Myung-Bo', 'Pohang'),
        ('South Korea', 'Huh Ki-Tae', 'Yukong'), 
        ('South Korea', 'Shin Tae-Yong', 'Ilhwa'),
        ('South Korea', 'Ko Jeong-Woon', 'Ilhwa'),
        ('South Korea', 'Kim Hyun-Seok', 'Ulsan'),
        ('South Korea', 'Kim Pan-Keun', 'LG'),
        ('Bosnia and Herzegovina', 'Amir Teljigović', 'Daewoo'), 
        ('South Korea', 'Hwang Sun-Hong', 'Pohang'),
        ('South Korea', 'Roh Sang-Rae', 'Chunnam'),
        ],
    1996: [  
        ('South Korea', 'Kim Byung-Ji', 'Ulsan'), 
        ('South Korea', 'Yoon Sung-Hyo', 'Suwon'),
        ('South Korea', 'Kim Joo-Sung', 'Busan'),
        ('South Korea', 'Huh Ki-Tae', 'Bucheon'), 
        ('South Korea', 'Shin Tae-Yong', 'Cheonan'),
        ('Romania', ' Pavel Badea', 'Suwon'),
        ('South Korea', 'Hong Myung-Bo', 'Pohang'),
        ('South Korea', 'Ha Seok-Ju', 'Busan'),
        ('South Korea', 'Kim Hyun-Seok', 'Ulsan'), 
        ('Serbia', 'Rade Bogdanović', 'Pohang'),
        ('Russia', 'Sergey Burdin', 'Bucheon'),
        ],
    
    1997: [  
        ('South Korea', 'Shin Bum-Chul', 'Busan'), 
        ('South Korea', 'Kim Joo-Sung', 'Busan'),
        ('Brazil', 'Maciel', 'Chunnam'),
        ('South Korea', 'Ahn Ik-Soo', 'Pohang'), 
        ('South Korea', 'Kim Hyun-Seok', 'Ulsan'),
        ('South Korea', 'Shin Jin-Won', 'Daejeon'),
        ('South Korea', 'Kim In-Wan', 'Chunnam'),
        ('South Korea', 'Lee Jin-Haeng', 'Suwon'),
        ('South Korea', 'Jung Jae-Kwon', 'Busan'), 
        ('Federal Republic of Yugoslavia', 'Radivoje Manic', 'Busan'),
        ('Ukraine', 'Serhiy Skachenko', 'Chunnam'),
        ],
    1998: [  
        ('South Korea', 'Kim Byung-Ji', 'Ulsan'), 
        ('South Korea', 'Ahn Ik-Soo', 'Pohang'),
        ('Brazil', 'Maciel', 'Chunnam'),
        ('South Korea', 'Lee Lim-Saeng', 'Bucheon'), 
        ('South Korea', 'Ko Jong-Soo', 'Suwon'),
        ('South Korea', 'Yoo Sang-Chul', 'Ulsan'),
        ('South Korea', 'Baek Seung-Chul', 'Pohang'),
        ('South Korea', 'Ahn Jung-Hwan', 'Busan'),
        ('South Korea', 'Jeong Jeong-Soo', 'Ulsan'), 
        ('South Korea', 'Kim Hyun-Seok', 'Ulsan'),
        ('Serbia and Montenegro', 'Saša Drakulić', 'Suwon'),
        ],
    1999: [  
        ('South Korea', 'Lee Woon-Jae', 'Suwon'), 
        ('South Korea', 'Kang Chul', 'Bucheon'),
        ('South Korea', 'Kim Joo-Sung', 'Busan'),
        ('Brazil', 'Maciel', 'Chunnam'),
        ('South Korea', 'Shin Hong-Gi', 'Suwon'),
        ('South Korea', 'Seo Jung-Won', 'Suwon'),
        ('South Korea', 'Ko Jong-Soo', 'Suwon'),
        ('Russia', 'Denis Laktionov', 'Suwon'),
        ('South Korea', 'Ko Jeong-Woon', 'Pohang'), 
        ('South Korea', 'Ahn Jung-Hwan', 'Busan'),
        ('Federal Republic of Yugoslavia', 'Saša Drakulić', 'Suwon'),
        ],
    2000: [  
        ('South Korea', 'Shin Eui-Son', 'Anyang'), 
        ('South Korea', 'Kang Chul', 'Bucheon'),
        ('South Korea', 'Lee Lim-Saeng', 'Bucheon'),
        ('South Korea', 'Kim Hyun-Soo', 'Seongnam'),
        ('Brazil', 'Maciel', 'Chunnam'), 
        ('Brazil', 'Andre', 'Anyang'),
        ('South Korea', 'Shin Tae-Yong', 'Seongnam'),
        ('South Korea', 'Jeon Kyung-Joon', 'Yukong'),
        ('Russia', 'Denis Laktionov', 'Suwon'), 
        ('South Korea', 'Choi Yong-Soo', 'Anyang'),
        ('South Korea', 'Kim Do-Hoon', 'Jeonbuk'),
        ],
    2001: [ 
        ('South Korea', 'Shin Eui-Son', 'Anyang'), 
        ('Federal Republic of Yugoslavia', 'Urumov', 'Busan'),
        ('South Korea', 'Kim Hyun-Soo', 'Seongnam'),
        ('South Korea', 'Kim Yong-Hee', 'Seongnam'),
        ('South Korea', 'Lee Young-Pyo', 'Anyang'), 
        ('South Korea', 'Shin Tae-Yong', 'Seongnam'),
        ('South Korea', 'Seo Jung-Won', 'Suwon'),
        ('South Korea', 'Song Chong-Gug', 'Busan'),
        ('South Korea', 'Nam Ki-Il', 'Bucheon'), 
        ('South Korea', 'Woo Sung-Yong', 'Busan'),
        ('Brazil', 'Sandro', 'Suwon'),
        ],
    2002: [ 
        ('South Korea', 'Lee Woon-Jae', 'Suwon'), 
        ('South Korea', 'Kim Hyun-Soo', 'Seongnam'),
        ('South Korea', 'Kim Tae-Young', 'Chunnam'),
        ('South Korea', 'Choi Jin-Cheul', 'Jeonbuk'),
        ('South Korea', 'Hong Myung-Bo', 'Pohang'), 
        ('South Korea', 'Shin Tae-Yong', 'Seongnam'),
        ('South Korea', 'Lee Chun-Soo', 'Ulsan'),
        ('Brazil', 'Andre', 'Anyang'),
        ('South Korea', 'Seo Jung-Won', 'Suwon'), 
        ('South Korea', 'Kim Dae-Eui', 'Seongnam'),
        ('South Korea', 'Yoo Sang-Chul', 'Ulsan'),
        ],
    2003: [ 
        ('South Korea', 'Seo Dong-Myung', 'Ulsan'), 
        ('South Korea', 'Choi Jin-Cheul', 'Jeonbuk'),
        ('South Korea', 'Kim Tae-Young', 'Chunnam'),
        ('South Korea', 'Kim Hyun-Soo', 'Seongnam'),
        ('Brazil', 'Santos', 'Pohang'), 
        ('South Korea', 'Shin Tae-Yong', 'Seongnam'),
        ('South Korea', 'Lee Seong-Nam', 'Seongnam'),
        ('South Korea', 'Lee Kwan-Woo', 'Daejeon'),
        ('South Korea', 'Kim Nam-Il', 'Chunnam'), 
        ('South Korea', 'Kim Do-Hoon', 'Seongnam'),
        ('Brazil', 'Magno Alves', 'Jeonbuk'),
        ],
    2004: [ 
        ('South Korea', 'Lee Woon-Jae', 'Suwon'), 
        ('Brazil', 'Santos', 'Pohang'),
        ('South Korea', 'Yoo Kyoung-Youl', 'Ulsan'),
        ('Argentina', 'Javier Musa', 'Suwon'),
        ('South Korea', 'Kwak Hee-Joo', 'Suwon'), 
        ('South Korea', 'Kim Dong-Jin', 'Seoul'),
        ('Brazil', 'Tavares', 'Pohang'),
        ('South Korea', 'Kim Do-Heon', 'Suwon'),
        ('South Korea', 'Kim Dae-Eui', 'Suwon'), 
        ('Brazil', 'Nádson', 'Suwon'),
        ('Brazil', 'Mota', 'Chunnam'),
        ],
    2005: [ 
        ('South Korea', 'Kim Byung-Ji', 'Pohang'), 
        ('South Korea', 'Im Joong-Yong', 'Incheon'),
        ('South Korea', 'Yoo Kyoung-You', 'Ulsan'),
        ('South Korea', 'Cho Yong-Hyung', 'Bucheon'),
        ('South Korea', 'Kim Young-Chul', 'Seongnam'), 
        ('South Korea', 'Lee Chun-Soo', 'Ulsan'),
        ('South Korea', 'Lee Ho', 'Ulsan'),
        ('South Korea', 'Kim Do-Heon', 'Seongnam'),
        ('South Korea', 'Cho Won-Hee', 'Suwon'), 
        ('South Korea', 'Park Chu-Young', 'Seoul'),
        ('Brazil', 'Leandro Machado', 'Ulsan'),
        ],
    2006: [ 
        ('South Korea', 'Park Ho-Jin', 'Suwon'), 
        ('South Korea', 'Jang Hak-Young', 'Seongnam'),
        ('Croatia', 'Mato Neretljak', 'Suwon'),
        ('South Korea', 'Choi Jin-Cheul', 'Jeonbuk'),
        ('South Korea', 'Kim Young-Chul', 'Seongnam'), 
        ('South Korea', 'Kim Do-Heon', 'Seongnam'),
        ('South Korea', 'Lee Kwan-Woo', 'Suwon'),
        ('South Korea', 'Baek Ji-Hoon', 'Suwon'),
        ('Brazil', 'Popo', 'Busan'), 
        ('South Korea', 'Woo Sung-Yong', 'Seongnam'),
        ('South Korea', 'Kim Eun-Jung', 'Seoul'),
        ],
    2007: [ 
        ('South Korea', 'Kim Byung-Ji', 'Seoul'), 
        ('Brazil', 'Adilson', 'Seoul'),
        ('Croatia', 'Mato Neretljak', 'Suwon'),
        ('South Korea', 'Hwang Jae-Won', 'Pohang'),
        ('South Korea', 'Jang Hak-Young', 'Seongnam'), 
        ('Brazil', 'Tavares', 'Pohang'),
        ('South Korea', 'Lee Kwan-Woo', 'Suwon'),
        ('South Korea', 'Kim Gi-Dong', 'Pohang'),
        ('South Korea', 'Kim Do-Heon', 'Seongnam'), 
        ('Brazil', 'Cabore', 'Gyeongnam'),
        ('South Korea', 'Lee Keun-Ho', 'Daegu'),
        ],
    2008: [ 
        ('South Korea', 'Lee Woon-Jae', 'Suwon'), 
        ('Brazil', 'Adilson', 'Seoul'),
        ('Croatia', 'Mato Neretljak', 'Suwon'),
        ('South Korea', 'Park Dong-Hyuk', 'Ulsan'),
        ('South Korea', 'Choi Hyo-Jin', 'Pohang'), 
        ('South Korea', 'Kim Hyung-Beom', 'Jeonbuk'),
        ('South Korea', 'Cho Won-Hee', 'Suwon'),
        ('South Korea', 'Ki Sung-Yueng', 'Seoul'),
        ('South Korea', 'Lee Chung-Yong', 'Seoul'), 
        ('Brazil', 'Edu', 'Suwon'),
        ('South Korea', 'Lee Keun-Ho', 'Daegu'),
        ],
    2009: [ 
        ('South Korea', 'Shin Hwa-Yong', 'Pohang'), 
        ('South Korea', 'Kim Sang-Sik', 'Jeonbuk'),
        ('South Korea', 'Kim Hyung-Il', 'Pohang'),
        ('South Korea', 'Hwang Jae-Won', 'Pohang'),
        ('South Korea', 'Choi Hyo-Jin', 'Pohang'), 
        ('South Korea', 'Choi Tae-Uk', 'Jeonbuk'),
        ('South Korea', 'Ki Sung-Yueng', 'Seoul'),
        ('South Korea', 'Kim Jung-Woo', 'Seongnam'),
        ('Brazil', 'Eninho', 'Jeonbuk'), 
        ('South Korea', 'Lee Dong-Gook', 'Jeonbuk'),
        ('Brazil', 'Denilson', 'Pohang'),
        ],
    
    2010: [ 
        ('South Korea', 'Kim Yong-Dae', 'Seoul'), 
        ('Brazil', 'Adilson', 'Seoul'),
        ('South Korea', 'Hong Jeong-Ho', 'Jeju'),
        ('Australia', 'Saša Ognenovski', 'Seongnam'),
        ('South Korea', 'Choi Hyo-Jin', 'Seoul'), 
        ('Colombia', 'Mauricio Molina', 'Seongnam'),
        ('South Korea', 'Yoon Bit-Garam', 'Gyeongnam'),
        ('South Korea', 'Koo Ja-Cheol', 'Jeju'),
        ('Brazil', 'Eninho', 'Jeonbuk'), 
        ('Montenegro', 'Dejan Damjanović', 'Seoul'),
        ('South Korea', 'Kim Eun-Jung', 'Jeju'),
        ],
    }
    
    
    
