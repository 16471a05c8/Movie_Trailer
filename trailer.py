import moviemedia
import fresh_tomatoes

aladdin=moviemedia.Animation("Aladdin",
                                                       "Story of Geany",
                                                          "https://i.ytimg.com/vi/BRpx72ycGXY/maxresdefault.jpg",
                                                      "https://www.youtube.com/watch?v=9g5knnlF7Zo" )
jayajanakinayaka=moviemedia.Animation("Jaya janaki nayaka",
                                      "story of family",
                                      "http://www.cinejosh.com/reviewsimg/big/jaya-janaki-nayaka-review_b_1108170645.jpg",
                                      "https://www.youtube.com/watch?v=uqkojQeXkZ8")
nanakuprematho=moviemedia.Animation("Nanaku prematho",
                                    "A story of father and son",
                                    "https://images.jdmagicbox.com/movies/mumbai_10718303102016_01_12_11_05_05.jpg",
                                 " https://www.youtube.com/watch?v=Om69gF1iiT4" )
srimantudu=moviemedia.Animation("Srimantudu",
                                "story of a undeveloped village",
                                "http://www.idlebrain.com/images5/wp-16srimanthudu1366.jpg",
                                "https://www.youtube.com/watch?v=EZGapI7yjh4")
jurrasicpark=moviemedia.Animation("Jurrasicpark",
                                  "park having dinosaraus",
                                  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBCXUKwpA4nkJZELF9WOtuptHkAFfU3rEx108VcSxOMIaA3xBu",
                             " https://www.youtube.com/watch?v=vn9mMeWcgoM" )
dhadak=moviemedia.Animation("dhadak",
                            "story","https://c.ndtvimg.com/ff59pro_dhadak-ndtv_625x300_26_July_18.jpg",
                           "https://www.youtube.com/watch?v=TIE92mUvSsw")
movies=[aladdin,jayajanakinayaka,nanakuprematho,srimantudu,jurrasicpark,dhadak]
fresh_tomatoes.open_movies_page(movies)
