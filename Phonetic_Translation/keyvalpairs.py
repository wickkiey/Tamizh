# Used from the below file 
# https://github.com/wickkiey/open-tamil/blob/main/tamil/utf8.py


import numpy as np

uyir_chars = {
    "அ":"a",
    "ஆ":"aa", 
    "இ":"i", 
    "ஈ":"ee" ,
    "உ":"u" ,
    "ஊ":"U", 
    "எ":"e", 
    "ஏ":"ea", 
    "ஐ":"ai" ,
    "ஒ":"o", 
    "ஓ":"O", 
    "ஔ":"au",
}

mei_chars = {
    "க்":"k",
    "ச்":"ch",
    "ட்":"t",
    "த்":"th",
    "ப்":"p",
    "ற்":"tr",
    "ஞ்":"nj",
    "ங்":"ng",
    "ண்":"nn",
    "ந்":"nh",
    "ம்":"m",
    "ன்":"n",
    "ய்":"y",
    "ர்":"r",
    "ல்":"l",
    "வ்":"v",
    "ழ்":"zh",
    "ள்":"l",
    "ஜ்":"j",
    "ஷ்":"sh",
    "ஸ்":"s",
    "ஹ்":"h",
    "க்ஷ்":"ksh"
}

tam_chars = ["க",
    "கா",
    "கி",
    "கீ",
    "கு",
    "கூ",
    "கெ",
    "கே",
    "கை",
    "கொ",
    "கோ",
    "கௌ",
    "ச",
    "சா",
    "சி",
    "சீ",
    "சு",
    "சூ",
    "செ",
    "சே",
    "சை",
    "சொ",
    "சோ",
    "சௌ",
    "ட",
    "டா",
    "டி",
    "டீ",
    "டு",
    "டூ",
    "டெ",
    "டே",
    "டை",
    "டொ",
    "டோ",
    "டௌ",
    "த",
    "தா",
    "தி",
    "தீ",
    "து",
    "தூ",
    "தெ",
    "தே",
    "தை",
    "தொ",
    "தோ",
    "தௌ",
    "ப",
    "பா",
    "பி",
    "பீ",
    "பு",
    "பூ",
    "பெ",
    "பே",
    "பை",
    "பொ",
    "போ",
    "பௌ",
    "ற",
    "றா",
    "றி",
    "றீ",
    "று",
    "றூ",
    "றெ",
    "றே",
    "றை",
    "றொ",
    "றோ",
    "றௌ",
    "ஞ",
    "ஞா",
    "ஞி",
    "ஞீ",
    "ஞு",
    "ஞூ",
    "ஞெ",
    "ஞே",
    "ஞை",
    "ஞொ",
    "ஞோ",
    "ஞௌ",
    "ங",
    "ஙா",
    "ஙி",
    "ஙீ",
    "ஙு",
    "ஙூ",
    "ஙெ",
    "ஙே",
    "ஙை",
    "ஙொ",
    "ஙோ",
    "ஙௌ",
    "ண",
    "ணா",
    "ணி",
    "ணீ",
    "ணு",
    "ணூ",
    "ணெ",
    "ணே",
    "ணை",
    "ணொ",
    "ணோ",
    "ணௌ",
    "ந",
    "நா",
    "நி",
    "நீ",
    "நு",
    "நூ",
    "நெ",
    "நே",
    "நை",
    "நொ",
    "நோ",
    "நௌ",
    "ம",
    "மா",
    "மி",
    "மீ",
    "மு",
    "மூ",
    "மெ",
    "மே",
    "மை",
    "மொ",
    "மோ",
    "மௌ",
    "ன",
    "னா",
    "னி",
    "னீ",
    "னு",
    "னூ",
    "னெ",
    "னே",
    "னை",
    "னொ",
    "னோ",
    "னௌ",
    "ய",
    "யா",
    "யி",
    "யீ",
    "யு",
    "யூ",
    "யெ",
    "யே",
    "யை",
    "யொ",
    "யோ",
    "யௌ",
    "ர",
    "ரா",
    "ரி",
    "ரீ",
    "ரு",
    "ரூ",
    "ரெ",
    "ரே",
    "ரை",
    "ரொ",
    "ரோ",
    "ரௌ",
    "ல",
    "லா",
    "லி",
    "லீ",
    "லு",
    "லூ",
    "லெ",
    "லே",
    "லை",
    "லொ",
    "லோ",
    "லௌ",
    "வ",
    "வா",
    "வி",
    "வீ",
    "வு",
    "வூ",
    "வெ",
    "வே",
    "வை",
    "வொ",
    "வோ",
    "வௌ",
    "ழ",
    "ழா",
    "ழி",
    "ழீ",
    "ழு",
    "ழூ",
    "ழெ",
    "ழே",
    "ழை",
    "ழொ",
    "ழோ",
    "ழௌ",
    "ள",
    "ளா",
    "ளி",
    "ளீ",
    "ளு",
    "ளூ",
    "ளெ",
    "ளே",
    "ளை",
    "ளொ",
    "ளோ",
    "ளௌ",
    "ஜ",
    "ஜா",
    "ஜி",
    "ஜீ",
    "ஜு",
    "ஜூ",
    "ஜெ",
    "ஜே",
    "ஜை",
    "ஜொ",
    "ஜோ",
    "ஜௌ",
    "ஷ",
    "ஷா",
    "ஷி",
    "ஷீ",
    "ஷு",
    "ஷூ",
    "ஷெ",
    "ஷே",
    "ஷை",
    "ஷொ",
    "ஷோ",
    "ஷௌ",
    "ஸ",
    "ஸா",
    "ஸி",
    "ஸீ",
    "ஸு",
    "ஸூ",
    "ஸெ",
    "ஸே",
    "ஸை",
    "ஸொ",
    "ஸோ",
    "ஸௌ",
    "ஹ",
    "ஹா",
    "ஹி",
    "ஹீ",
    "ஹு",
    "ஹூ",
    "ஹெ",
    "ஹே",
    "ஹை",
    "ஹொ",
    "ஹோ",
    "ஹௌ",
    "க்ஷ",
    "க்ஷா",
    "க்ஷி",
    "க்ஷீ",
    "க்ஷு",
    "க்ஷூ",
    "க்ஷெ",
    "க்ஷே",
    "க்ஷை",
    "க்ஷொ",
    "க்ஷோ",
    "க்ஷௌ"]

ayuth = "ஃ"