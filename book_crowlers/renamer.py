import os

list = {'Ҡайырылмаһын ҡанаттар.djvu': 'qajyrylmahyn_qanattar.djvu',
        'Йәш ғаиләгә нәсихәттәр.docx': 'jash_ghailaga_nasihattar.docx',
        'Әфлисун тәме.djvu': 'aflisun_tame.djvu',
        'Һайланма әҫәрҙәр.doc': 'hajlanma_acarzar.doc',
        'Тел хикмәттәре.docx': 'tel_hikmattare.docx',
        'Эш алтында түгел.djvu': 'esh_altynda_tugel.djvu',
        'Һүнгән йондоҙ яҡтыһы.docx': 'hungan_jondoz_yaqtyhy.docx',
        'Китәбүт-тәрбиә (Тәрбиә китабы).docx': 'kitabut-tarbia_(tarbia_kitaby).docx',
        'Башланмыш (Книга бытия на башкирском языке).epub': 'bashlanmysh_(kniga_bytiya_na_bashkirskom_yazyke).epub',
        'Башҡорт теленең академик һүҙлеге II том.djvu': 'bashqort_teleneng_akademik_huzlege_ii_tom.djvu',
        'Башҡортса-русса һүҙлек.djvu': 'bashqortsa-russa_huzlek.djvu',
        'Башҡорт теленең антонимдар һүҙлеге.djvu': 'bashqort_teleneng_antonimdar_huzlege.djvu',
        'Нәсихәттәр.djvu': 'nasihattar.djvu',
        'Ҡөрьән тәфсире.doc': 'qoran_tafsire.doc',
        'Ҡурсаулыҡ һуҡмаҡтарында.epub': 'qursaulyq_huqmaqtarynda.epub',
        'Хужа Насретдин мәҙәктәре.fb2': 'huja_nasretdin_mazaktare.fb2',
        'Башҡорт теленең фразеологик һүҙлеге.djvu': 'bashqort_teleneng_frazeologik_huzlege.djvu',
        'Башҡортса - русса һүҙлек (2200 һүҙ).djvu': 'bashqortsa_-_russa_huzlek_(2200_huz).djvu',
        'Башҡорт әҙәбиәте тарихы. Хәҙерге әҙәбиәт.doc': 'bashqort_azabiate_tarihy._hazerge_azabiat.doc',
        'Китапхана дәресе.doc': 'kitaphana_darese.doc',
        'Йәш быунға белем.doc': 'jash_byungha_belem.doc',
        'Шәғәле Шаһман нәҫеле.docx ,Шәғәле Шаһман нәҫеле.txt': 'shaghale_shahman_nacele.docx_,shaghale_shahman_nacele.txt',
        'Халҡыбыҙҙың этнодемографик үҫеше хаҡында уйланыуҙар һәм күҙәтеүҙәр.doc': 'halqybyzzyng_etnodemografik_uceshe_haqynda_ujlanyuzar_ham_kuzateuzar.doc',
        'Зәңгәр катер: роман, хикәйәләр һәм хикмәттәр..djvu': 'zanggar_kater:_roman,_hikajalar_ham_hikmattar..djvu',
        'С песней идут солдаты.doc': 's_pesnej_idut_soldaty.doc',
        'Башҡорт әҙәбиәтендә һүрәтләү саралары (әҙәби эшмәкәрлек мәсьәләләре).doc': 'bashqort_azabiatenda_huratlau_saralary_(azabi_eshmakarlek_masalalare).doc',
        'Мәғрифәт усағының яҡтыһы  .doc': 'maghrifat_usaghynyng_yaqtyhy__.doc',
        'Ҡан.epub': 'qan.epub',
        'ӘЛ-ҠИССА БУҘЙЕГЕТ.fb2': 'al-qissa_buzjeget.fb2',
        'Һайланма әҫәрҙәр (төҙөүсеһе И. Ә. Шарапов).doc': 'hajlanma_acarzar_(tozousehe_i._a._sharapov).doc',
        'Ҡуласа.txt': 'qulasa.txt',
        'Башҡорт тарихы.djvu': 'bashqort_tarihy.djvu',
        'Эш алтында түгел: Хикәйәләр..doc': 'esh_altynda_tugel:_hikajalar..doc',
        'Ирәндек мондары.doc': 'irandek_mondary.doc',
        'Башҡорт абыздары һәм батырҙары.doc': 'bashqort_abyzdary_ham_batyrzary.doc',
        'Әҫәрҙәр. Өс томда, I том. Шиғырҙар, поэмалар..epub ,Әҫәрҙәр. Өс томда, I том. Шиғырҙар, поэмалар..txt': 'acarzar._os_tomda,_i_tom._shighyrzar,_poemalar..epub_,acarzar._os_tomda,_i_tom._shighyrzar,_poemalar..txt',
        'Минең телем.doc': 'mineng_telem.doc',
        'Шәйехзада Бабич — һүҙ оҫтаһы .docx': 'shajehzada_babich_—_huz_octahy_.docx',
        'Балалар фольклоры: Бала саҡ — уйнап-көлоп үҫер сңҡ.djvu': 'balalar_folklory:_bala_saq_—_ujnap-kolop_ucer_sngq.djvu',
        'Быҫҡаҡ ямғыр.txt': 'bycqaq_yamghyr.txt',
        'Библиографик күрһәткес.doc': 'bibliografik_kurhatkes.doc',
        'Америка-Азия телдәре  араһында параллелдәр.djvu': 'amerika-aziya_teldare__arahynda_paralleldar.djvu',
        'Әй һәи Йүрүҙән буйы башҡорттарының шәжәрәләре.doc': 'aj_hai_juruzan_bujy_bashqorttarynyng_shajaralare.doc',
        'Ҡолой кантон.djvu': 'qoloj_kanton.djvu',
        'Намаҙ уҡыу тәртибе.djvu': 'namaz_uqyu_tartibe.djvu',
        'Ғәрәб яҙмаһың өйрәнеүселәргә әлифба.djvu': 'gharab_yazmahyng_ojraneuselarga_alifba.djvu',
        'Дәүләкән ынйылары.doc': 'daulakan_ynjylary.doc',
        'Урыҫса-башҡортса һүҙлек: 2 томда. 1-се том. А-О.djvu': 'urycsa-bashqortsa_huzlek:_2_tomda._1-se_tom._a-o.djvu',
        'Урыҫса-башҡортса һүҙлек: 2 томда. 2-се том. П-Я.djvu': 'urycsa-bashqortsa_huzlek:_2_tomda._2-se_tom._p-ya.djvu',
        'Телем минең – яҙмышым .djvu': 'telem_mineng_–_yazmyshym_.djvu',
        'Йыр һәм ер улы Мөхәмәтйән Ҡаҙакбаев.docx': 'jyr_ham_er_uly_mohamatjan_qazakbaev.docx',
        'Артыҡбикә.doc': 'artyqbika.doc',
        'Йәмғиәтте Тотоп Торған Рухи Бағана.doc': 'jamghiatte_totop_torghan_ruhi_baghana.doc',
        'Бөйөк төрки телебеҙ.doc': 'bojok_torki_telebez.doc',
        'Донъя Уралдан башлана.doc': 'donya_uraldan_bashlana.doc',
        'Драмалар.docx': 'dramalar.docx',
        'НАчало начал. .doc': 'nachalo_nachal._.doc',
        'Салауат Юлаев шәжәрәһен тергеҙеү.doc': 'salauat_yulaev_shajarahen_tergezeu.doc',
        'Шәжәрәләр.docx': 'shajaralar.docx',
        'Ырып яҙған ырындарыбыҙ.doc': 'yryp_yazghan_yryndarybyz.doc',
        'Ҡолонташ.djvu': 'qolontash.djvu',
        'Хәтерҙәге яҡты  миҙгелдәр .djvu': 'haterzage_yaqty__mizgeldar_.djvu',
        'Арғымаҡ.djvu': 'arghymaq.djvu',
        'ТАШТУҒАЙ.djvu': 'tashtughaj.djvu',
        'Нәсихәттәр.doc': 'nasihattar.doc',
        'Мишәр башҡорттары.doc': 'mishar_bashqorttary.doc',
        'Төп халыҡ хоҡуҡтары.doc': 'top_halyq_hoquqtary.doc',
        'Мин кем икән? Их, беләһе килә.doc': 'min_kem_ikan?_ih,_belahe_kila.doc',
        'Туй йолалары.djvu': 'tuj_jolalary.djvu',
        'Әхмәтзәки Вәлиди Туған. Тарихи- биографик китап.doc': 'ahmatzaki_validi_tughan._tarihi-_biografik_kitap.doc',
        'Башҡорт тарихы донья китабына язылган.doc': 'bashqort_tarihy_donya_kitabyna_yazylgan.doc',
        'Рәжәпов Р. Ф.doc': 'rajapov_r._f.doc',
        'Атлы башҡорт.djvu': 'atly_bashqort.djvu',
        'Ҡапҡан: Мажаралы фантастик повестар.fb2': 'qapqan:_majaraly_fantastik_povestar.fb2',
        'Сит планета ҡыҙы.docx': 'sit_planeta_qyzy.docx',
        'Риүәйәт һәм легендаларҙа халыҡ тарихы.doc': 'riuajat_ham_legendalarza_halyq_tarihy.doc',
        'ауылдар тарихы — кешеләр яҙмышы.doc': 'auyldar_tarihy_—_keshelar_yazmyshy.doc',
        'ТИРМӘКӘЙ.djvu': 'tirmakaj.djvu',
        ' Оҙон-оҙаҡ бала саҡ.docx': '_ozon-ozaq_bala_saq.docx',
        'Һайланма мәҡәлдәр.doc': 'hajlanma_maqaldar.doc',
        'Башҡортостанда йәшәгән халыҡтар күпселеге - башҡорттар.doc': 'bashqortostanda_jashagan_halyqtar_kupselege_-_bashqorttar.doc',
        'Исемдәр донъяһында. Башҡорт исемдәре һүҙлеге, башҡорт һәм рус телдәрендә.fb2': 'isemdar_donyahynda._bashqort_isemdare_huzlege,_bashqort_ham_rus_teldarenda.fb2',
        'Туйҙың бер көнө.doc': 'tujzyng_ber_kono.doc',
        'Ҡиссаи Йософ.epub': 'qissai_josof.epub',
        'Егерменсе быуаттың утыҙынсы йылдарында башҡорт əҙəбиəте (төп үҫеш тенденциялары һəм герой проблемаһы).doc': 'egermense_byuattyng_utyzynsy_jyldarynda_bashqort_əzəbiəte_(top_ucesh_tendentsiyalary_həm_geroj_problemahy).doc',
        'Башҡорт кәбиләләре тарихынан.doc': 'bashqort_kabilalare_tarihynan.doc',
        'Тамырҙарыбыҙ - тәрәндә.doc': 'tamyrzarybyz_-_taranda.doc',
        ' Тәмле-тәмле-тәмлекәс:.djvu': '_tamle-tamle-tamlekas:.djvu',
        'Әсә теле.djvu': 'asa_tele.djvu',
        'Урал батыр.docx': 'ural_batyr.docx',
        'Арғымаҡ.docx': 'arghymaq.docx',
        'Французик.docx': 'frantsuzik.docx',
        'Ҡарт тѳлкѳ.docx': 'qart_tѳlkѳ.docx',
        'Мөхәббәт.docx': 'mohabbat.docx',
        'Башҡорттар.docx': 'bashqorttar.docx',
        'Шөңгөрлө барабан.docx': 'shonggorlo_baraban.docx',
        'Таң атҡанда.docx': 'tang_atqanda.docx',
        'Үҫтекәй.docx': 'uctekaj.docx',
        'Айбикә.docx': 'ajbika.docx',
        'Ҡарт менән диңгеҙ.docx': 'qart_menan_dinggez.docx',
        'Көн башы һуҡмаҡтары.docx': 'kon_bashy_huqmaqtary.docx',
        'Атайымдың өс һәнәге.docx': 'atajymdyng_os_hanage.docx',
        'Өс таған.docx': 'os_taghan.docx',
        'Дуҫ булайыҡ.docx': 'duc_bulajyq.docx',
        'Яныу.docx': 'yanyu.docx',
        'Бөркөт саңҡыуы.pdf.djvu': 'borkot_sangqyuy.pdf.djvu',
        'Ҡөрьән уҡырға өйрәнәбеҙ.docx': 'qoran_uqyrgha_ojranabez.docx',
        'Шәйех нәүәиҙең 40 хәҙисе.doc': 'shajeh_nauaizeng_40_hazise.doc',
        'Аятел Көрси .doc': 'ayatel_korsi_.doc',
        'Башланмыш.fb2': 'bashlanmysh.fb2',
        'Һәфтиәк шәриф.doc': 'haftiak_sharif.doc',
        'Тәрбиә китабы.doc': 'tarbia_kitaby.doc',
        'Ислам дине.doc': 'islam_dine.doc',
        'Тәрбиә китабы.fb2': 'tarbia_kitaby.fb2',
        'Йософ.epub': 'josof.epub',
        'Ҡисса Йософ.epub': 'qissa_josof.epub',
        'Әфлисун тәме: шиғырҙар, хикәйәләр.fb2': 'aflisun_tame:_shighyrzar,_hikajalar.fb2',
        'Газин Ф. С..fb2': 'gazin_f._s..fb2',
        'һүнгән йондоҙ яҡтыһы.epub': 'hungan_jondoz_yaqtyhy.epub',
        'Сёфёртуй яланы.epub': 'sefertuj_yalany.epub',
        'Фәрештәм минең.epub': 'fareshtam_mineng.epub',
        'Яттар мөһөрө.epub': 'yattar_mohoro.epub',
        'Болан балаһы.epub': 'bolan_balahy.epub',
        'Ил сигендә йәшәгән ҡарттың аты юғалды.epub': 'il_sigenda_jashagan_qarttyng_aty_yughaldy.epub',
        'Бер кәмәлә.epub': 'ber_kamala.epub',
        'Һағынырһың — мин булмам.epub': 'haghynyrhyng_—_min_bulmam.epub',
        'Көнгәккә сығыу.epub': 'kongakka_syghyu.epub',
        'Миңа Париждан алып ҡайт....epub': 'minga_parijdan_alyp_qajt....epub',
        'Сатирик пенсияха сы-ха-ха!.epub': 'satirik_pensiyaha_sy-ha-ha!.epub',
        'Сөкәк.epub': 'sokak.epub',
        'Ҡыҙғансыҡ.epub': 'qyzghansyq.epub',
        'Эстафета.epub': 'estafeta.epub',
        'Батырҙар тураһында әкиәттәр.epub': 'batyrzar_turahynda_akiattar.epub',
        'Хайуандар тураһында әкиәттәр.epub': 'hajuandar_turahynda_akiattar.epub',
        'Тормош көнкүреш әкиәттәре.epub': 'tormosh_konkuresh_akiattare.epub',
        'Тылсымлы әкиәттәр.epub': 'tylsymly_akiattar.epub',
        'ШӘҒӘЛЕ ШАҺМАН НӘҪЕЛЕ.djvu': 'shaghale_shahman_nacele.djvu',
        'ШОФЕРҘАРҘЫ  ЮЛ ҒАЗАПТАРЫНАН ҺАҠЛАУСЫ ДОҒАЛАР ҮӘ АЯТТАР .doc': 'shoferzarzy__yul_ghazaptarynan_haqlausy_doghalar_ua_ayattar_.doc',
        'Башҡорт халыҡ ижады. Бәйеттәр, йырҙар, таҡмаҡтар.doc': 'bashqort_halyq_ijady._bajettar,_jyrzar,_taqmaqtar.doc',
        'АҠБУҘАТ.docx': 'aqbuzat.docx',
        'Аҫылғужа - Биобиблиографик күрһәткес.doc': 'acylghuja_-_biobibliografik_kurhatkes.doc',
        'Тәүәккәллек һәм рух менән һуғарылған сәйәхәт.doc': 'tauakkallek_ham_ruh_menan_hugharylghan_sajahat.doc',
        'Башҡорт аш-һыуҙары лексикаһы.djvu': 'bashqort_ash-hyuzary_leksikahy.djvu',
        'Башҡорт яҙыуы тарихынан.djvu': 'bashqort_yazyuy_tarihynan.djvu',
        'Ай менән Зөһрә.djvu': 'aj_menan_zohra.djvu',
        'Аҡмулланы төшөмдә күрҙем.djvu': 'aqmullany_toshomda_kurzem.djvu',
        'Әлли-бәлли, бәү-бәү.djvu': 'alli-balli,_bau-bau.djvu',
        'Алма бабай һабаҡтары.djvu': 'alma_babaj_habaqtary.djvu',
        'Ҡалдырма, әсәй!.djvu': 'qaldyrma,_asaj!.djvu',
        'Күңелле бала саҡ.djvu': 'kungelle_bala_saq.djvu',
        'Шалҡан.djvu': 'shalqan.djvu',
        'Шәпәй менән шайтан.djvu': 'shapaj_menan_shajtan.djvu',
        'Шоколад ниңә асыуланды?.djvu': 'shokolad_ninga_asyulandy?.djvu',
        'Һөнәрсе менән өйрәнсек.djvu': 'honarse_menan_ojransek.djvu',
        'Зиннурова Әлфиә.djvu': 'zinnurova_alfia.djvu',
        'АҘНАМӨХӘМӘТ, САЛАУАТ ҺӘМ ЮЛАЙ ЙОНДОҘЛОҒО.doc': 'aznamohamat,_salauat_ham_yulaj_jondozlogho.doc',
        'Бөйөк төрки.doc': 'bojok_torki.doc',
        'Әҫәрҙәр ун дүрт томда. Йәшлек тураһында йыр.doc': 'acarzar_un_durt_tomda._jashlek_turahynda_jyr.doc',
        'ете томда, том III. Тулҡын өҫтөндәге күбектәр.doc': 'ete_tomda,_tom_iii._tulqyn_octondage_kubektar.doc',
        'Әҫәрҙәр ун дүрт томда, том IX. Коммунист. Роман һәм повестәр.doc': 'acarzar_un_durt_tomda,_tom_ix._kommunist._roman_ham_povestar.doc',
        'Әҫәрҙәр ун дүрт томда, том IX. Коммунист.doc': 'acarzar_un_durt_tomda,_tom_ix._kommunist.doc',
        'Әҫәрҙәр ун биш томда, ХV том. Көҙгө япраҡтар. Тарих, публицистика.doc': 'acarzar_un_bish_tomda,_hv_tom._kozgo_yapraqtar._tarih,_publitsistika.doc',
        'ӘҪӘРҘӘР УН ДҮРТ ТОМДА. ТОМ VII.doc': 'acarzar_un_durt_tomda._tom_vii.doc',
        'Әҫәрҙәр ун дүрт томда, том XIV. Тамырҙар. Башҡорт халҡына көҙгө.doc': 'acarzar_un_durt_tomda,_tom_xiv._tamyrzar._bashqort_halqyna_kozgo.doc',
        'Әҫәрҙәр ун дүрт томда, ХII том. Заманалар. Башҡорт халҡына көҙгө.doc': 'acarzar_un_durt_tomda,_hii_tom._zamanalar._bashqort_halqyna_kozgo.doc',
        'Әҫәрҙәр ун дүрт томда, VIII том. Заман һәм замандаштар.doc': 'acarzar_un_durt_tomda,_viii_tom._zaman_ham_zamandashtar.doc',
        'Ерем, кешеләрем. Роман.doc': 'erem,_keshelarem._roman.doc',
        'Әҫәрҙәр ун биш томда, том I. Йылдарым һәм моңдарым. Шиғырҙар.docx': 'acarzar_un_bish_tomda,_tom_i._jyldarym_ham_mongdarym._shighyrzar.docx',
        'ӘҪӘРҘӘР УН ДҮРТ ТОМДА  ТОМ XI.doc': 'acarzar_un_durt_tomda__tom_xi.doc',
        'Әҫәрҙәр ун биш томда, XIII том. Заманалар. Башҡорт халҡына көҙгө.doc': 'acarzar_un_bish_tomda,_xiii_tom._zamanalar._bashqort_halqyna_kozgo.doc',
        'ЯТЛАҒАНДАРҒА ЯДКӘР.doc': 'yatlaghandargha_yadkar.doc',
        'БОЛАН  БАЛАҺЫ.doc': 'bolan__balahy.doc',
        'Тел хикмәттәре.fb2': 'tel_hikmattare.fb2',
        'Башҡорт халҡының тарихы.doc': 'bashqort_halqynyng_tarihy.doc',
        'Ҡалдырма, әсәй!.doc': 'qaldyrma,_asaj!.doc',
        'Халҡым хазинаһы: очерктар.doc': 'halqym_hazinahy:_ocherktar.doc',
        'МӨХӘББӘТ.docx': 'mohabbat.docx',
        'Башҡорт көсө.doc': 'bashqort_koso.doc',
        'Аҡ менән ҡара.djvu': 'aq_menan_qara.djvu',
        'Башҡорттар тарихы (автор ҡулъяҙмаһынан тәржемә.docx': 'bashqorttar_tarihy_(avtor_qulyazmahynan_tarjema.docx',
        'Әбйәлил.docx': 'abjalil.docx',
        'Әхмәт жулик.docx': 'ahmat_julik.docx',
        'Айыу менән бал ҡорттары.docx': 'ajyu_menan_bal_qorttary.docx',
        'Айыу өйө.docx': 'ajyu_ojo.docx',
        'Аҡҡош һөтө.docx': 'aqqosh_hoto.docx',
        'Аҡман-Тоҡман.docx': 'aqman-toqman.docx',
        'Аҡыллы бесәй менән таҙ.docx': 'aqylly_besaj_menan_taz.docx',
        'Ала ҡарға.docx': 'ala_qargha.docx',
        'Алдар батыр менән генерал.docx': 'aldar_batyr_menan_general.docx',
        'Алдар төлкө.docx': 'aldar_tolko.docx',
        'Алдарҙың ер һатҡаны.docx': 'aldarzyng_er_hatqany.docx',
        'Алдарҙың ен ҡыуғаны.docx': 'aldarzyng_en_qyughany.docx',
        'Алтын ашыҡ.docx': 'altyn_ashyq.docx',
        'Алтынҡойроҡ-көмөшъял.docx': 'altynqojroq-komoshyal.docx',
        'Алтын сәсле егет.docx': 'altyn_sasle_eget.docx',
        'Алтынсәс.docx': 'altynsas.docx',
        'Бар ине заманалар.djvu': 'bar_ine_zamanalar.djvu',
        'Башҡортса һөйләшәбеҙ.djvu': 'bashqortsa_hojlashabez.djvu',
        'Йәшәргә ваҡыт: повестар, хикәйәләр һәм эсселар .djvu': 'jasharga_vaqyt:_povestar,_hikajalar_ham_esselar_.djvu',
        'Башҡорт халыҡ әкиәттәре.docx': 'bashqort_halyq_akiattare.docx',
        'УРАЛ ИЛЕНДӘ.djvu': 'ural_ilenda.djvu',
        'Витамин ҡайҙа үҫә?.djvu': 'vitamin_qajza_uca?.djvu',
        'Vitamin qajza usa?.djvu': 'vitamin_qajza_usa?.djvu',
        'Bashqortostan tarihy: Borongho zamandarzan XIX byuat azaghyna tiklem. 8 klass oson dareslek.doc': 'bashqortostan_tarihy:_borongho_zamandarzan_xix_byuat_azaghyna_tiklem._8_klass_oson_dareslek.doc',
        'Vitamin qajza usa.djvu': 'vitamin_qajza_usa.djvu',
        'milash_talgashtare_shighyrzar.djvu': 'milash_talgashtare_shighyrzar.djvu',
        'mohammat_iskuzhin_turahynda.doc': 'mohammat_iskuzhin_turahynda.doc',
        'min_postamyn,_vatan_bashqortostandyng_halyq_shaghiry_rashit_nighmatizeng_100_jyllyq_yubilejyna_arnalghan_jyjyntyq.doc': 'min_postamyn,_vatan_bashqortostandyng_halyq_shaghiry_rashit_nighmatizeng_100_jyllyq_yubilejyna_arnalghan_jyjyntyq.doc',
        'bashqort_tarihy.doc': 'bashqort_tarihy.doc',
        'bashqort_azabiate_antologiyahy,_ike_tomda._ii_tom._hix_byuat.docx': 'bashqort_azabiate_antologiyahy,_ike_tomda._ii_tom._hix_byuat.docx',
        'arghayash_fazhighahe.doc': 'arghayash_fazhighahe.doc',
        'tonyak_bashkortlary.doc': 'tonyak_bashkortlary.doc',
        'dialkt_tele_ham_azabi_tel.doc': 'dialkt_tele_ham_azabi_tel.doc',
        'tonyaqkonbajysh_bashqorttarynyng_balalaryn_bashqort_telenda_uqytyu_masalahena_qarata.doc': 'tonyaqkonbajysh_bashqorttarynyng_balalaryn_bashqort_telenda_uqytyu_masalahena_qarata.doc',
        'onottorolghan_dan_tarihybyz.doc': 'onottorolghan_dan_tarihybyz.doc',
        'bashqort_teleneng_konbajysh_dialekty.doc': 'bashqort_teleneng_konbajysh_dialekty.doc',
        'hojlasha_belgan_kanfit_akiattar.djvu': 'hojlasha_belgan_kanfit_akiattar.djvu',
        'on_ham_han.djvu': 'on_ham_han.djvu',
        'qyzyqly_osrashyuzar.djvu': 'qyzyqly_osrashyuzar.djvu',
        'aq_ham_qara.djvu': 'aq_ham_qara.djvu',
        '_haterzage_yaqty_mizgeldar.djvu': '_haterzage_yaqty_mizgeldar.djvu',
        'tirajun_menan_tanysham.djvu': 'tirajun_menan_tanysham.djvu',
        'terpekaj_sajahate.djvu': 'terpekaj_sajahate.djvu',
        'tauge_dares.djvu': 'tauge_dares.djvu',
        'mongtalgash.djvu': 'mongtalgash.djvu',
        'sysqansyq_menan_sysqansuq_mazharalary.djvu': 'sysqansyq_menan_sysqansuq_mazharalary.djvu',
        'saksak_menan_bauyrhaq_nisek_tamle_rizyq_azerlarga_ojrande..djvu': 'saksak_menan_bauyrhaq_nisek_tamle_rizyq_azerlarga_ojrande..djvu',
        'qolontash.djvu': 'qolontash.djvu',
        'ujnaj_jajghor_nurzary.djvu': 'ujnaj_jajghor_nurzary.djvu',
        '_ej_ghumer_yuldary.djvu': '_ej_ghumer_yuldary.djvu',
        'tashqyn_urtahynda.djvu': 'tashqyn_urtahynda.djvu',
        'keshe_dramahy.djvu': 'keshe_dramahy.djvu',
        'olasajem_akiattare.djvu': 'olasajem_akiattare.djvu',
        'ofoqtaghy_jondoz_yaqtyhy.djvu': 'ofoqtaghy_jondoz_yaqtyhy.djvu',
        'hajlanma_asarzar_9_tom.djvu': 'hajlanma_asarzar_9_tom.djvu',
        'jajge_sella.djvu': 'jajge_sella.djvu',
        'hungghy_osrashyu.djvu': 'hungghy_osrashyu.djvu',
        'nazgol.djvu': 'nazgol.djvu',
        'altyn_quraj.djvu': 'altyn_quraj.djvu',
        'bezzeng_ojzong_jame.djvu': 'bezzeng_ojzong_jame.djvu',
        'hajlanma_asarzar,_durtense_tom.djvu': 'hajlanma_asarzar,_durtense_tom.djvu',
        'kungelem_jyly_telaj.djvu': 'kungelem_jyly_telaj.djvu',
        'qyu_qaraghas.djvu': 'qyu_qaraghas.djvu',
        'asarzar_5_tom.djvu': 'asarzar_5_tom.djvu',
        'botabezga_ber_er_shary.djvu': 'botabezga_ber_er_shary.djvu',
        'quyan_bazarza_nisek_bure_hatqan.djvu': 'quyan_bazarza_nisek_bure_hatqan.djvu',
        'urman_jyry.djvu': 'urman_jyry.djvu',
        '_donyasygym_shighyrzar.djvu': '_donyasygym_shighyrzar.djvu',
        'kungelle_irta.djvu': 'kungelle_irta.djvu',
        'kalendar_ham_hynamyshtar.djvu': 'kalendar_ham_hynamyshtar.djvu',
        'joragemda_synglar_ber_jyr.djvu': 'joragemda_synglar_ber_jyr.djvu',
        'jashel_siramda_hary_kerandil.djvu': 'jashel_siramda_hary_kerandil.djvu',
        'min_uzemmen_haman.djvu': 'min_uzemmen_haman.djvu',
        'ghumer_kitaby.djvu': 'ghumer_kitaby.djvu',
        'vitamin_qajza_usa.djvu': 'vitamin_qajza_usa.djvu',
        '_hajrahyn_burandarym.djvu': '_hajrahyn_burandarym.djvu',
        'zamanyna_kura_kolkoho.djvu': 'zamanyna_kura_kolkoho.djvu',
        'hajlanma_asarzar._berense_tom..djvu': 'hajlanma_asarzar._berense_tom..djvu',
        'belgem_kila_botaheng.djvu': 'belgem_kila_botaheng.djvu',
        'ghumer_kisenuzare.djvu': 'ghumer_kisenuzare.djvu',
        'ural_ilenda.djvu': 'ural_ilenda.djvu',
        'bashqortsa_hojlashabez.djvu': 'bashqortsa_hojlashabez.djvu',
        'bashqort_teleneng_akademik_huzlege._1_tom.djvu': 'bashqort_teleneng_akademik_huzlege._1_tom.djvu',
        'bar_ine_zamanalar.djvu': 'bar_ine_zamanalar.djvu',
        'aflisun_tame.djvu': 'aflisun_tame.djvu',
        'shapaj_menan_shajtan.djvu': 'shapaj_menan_shajtan.djvu',
        'bortoklap_jyjyla_altyn.docx': 'bortoklap_jyjyla_altyn.docx',
        'aj_menan_zohra.epub': 'aj_menan_zohra.epub',
        'qaldyrma_asaj.epub': 'qaldyrma_asaj.epub',
        'shapaj_menan_shajtan.epub': 'shapaj_menan_shajtan.epub',
        'olatajzarzyng_bar_tarihy..djvu': 'olatajzarzyng_bar_tarihy..djvu',
        'yaua_zanggar_qarzar..djvu': 'yaua_zanggar_qarzar..djvu',
        'quzyjkurpas._ofo._1965.djvu': 'quzyjkurpas._ofo._1965.djvu',
        'hin_aq_qajyn_yanynda_tora_ineng._ofo.2007.djvu': 'hin_aq_qajyn_yanynda_tora_ineng._ofo.2007.djvu',
        'tau_artynda_nizar_bar._ofo._1997.djvu': 'tau_artynda_nizar_bar._ofo._1997.djvu',
        'ej_yajyq_jort,_yajyq_jort._ofo._1998.djvu': 'ej_yajyq_jort,_yajyq_jort._ofo._1998.djvu',
        'sysqansyq_menan_sysqansuq_mazharalary.epub': 'sysqansyq_menan_sysqansuq_mazharalary.epub',
        'quyan_bazarza_nisek_bure_hatqan.epub': 'quyan_bazarza_nisek_bure_hatqan.epub',
        '_alifba.djvu': '_alifba.djvu',
        '...kuz_halamyn_halqyma.docx': '...kuz_halamyn_halqyma.docx',
        'telem_mineng__yazmyshym.doc': 'telem_mineng__yazmyshym.doc',
        'milashkalash.docx': 'milashkalash.docx',
        'maqaldar_ham_ajtemdar.docx': 'maqaldar_ham_ajtemdar.docx',
        'halyq_shaghiry__halyq_haterenda.djvu': 'halyq_shaghiry__halyq_haterenda.djvu',
        'ural_ilenda.epub': 'ural_ilenda.epub',
        'ese_qar.fb2': 'ese_qar.fb2',
        'tataj_qalaq_bazarza.djvu': 'tataj_qalaq_bazarza.djvu',
        'sejalek_jyry_shighyrzar.djvu': 'sejalek_jyry_shighyrzar.djvu',
        'bashqorttar_tarihy.txt': 'bashqorttar_tarihy.txt',
        'asarzar_1917_jylgha_qazar_yazylghan_asarzare.txt': 'asarzar_1917_jylgha_qazar_yazylghan_asarzare.txt',
        'bashqort_koso.doc': 'bashqort_koso.doc',
        'hajlanma_asarzar.docx': 'hajlanma_asarzar.docx',
        'asqyn_rajony_ham_qasabahy.doc': 'asqyn_rajony_ham_qasabahy.doc',
        'bolan_balahy.doc': 'bolan_balahy.doc',
        'bashlanmysh.epub': 'bashlanmysh.epub',
        'yahya_taghbir_itkan_inzhel.docx': 'yahya_taghbir_itkan_inzhel.docx',
        'blyuda_bashkirskoj_kuhni.djvu': 'blyuda_bashkirskoj_kuhni.djvu',
        'min_postamyn,_vatan.doc': 'min_postamyn,_vatan.doc',
        'bashqort_halqynyng_tarihy_ham_azatlyq_korashe.doc': 'bashqort_halqynyng_tarihy_ham_azatlyq_korashe.doc',
        'bashqortostan_tarihy.doc': 'bashqortostan_tarihy.doc',
        'zabih_isquzhindy_belahengme.doc': 'zabih_isquzhindy_belahengme.doc',
        'qan_auazy.epub': 'qan_auazy.epub',
        'qan_auazy.docx': 'qan_auazy.docx',
        'kondalek_bittarenan..djvu': 'kondalek_bittarenan..djvu',
        'bashkirskie_suveniry._bashqort_suvenirzare._ofo.1982.djvu': 'bashkirskie_suveniry._bashqort_suvenirzare._ofo.1982.djvu',
        'hazhiahmat_unasov._qanly_jyldar._2011.djvu': 'hazhiahmat_unasov._qanly_jyldar._2011.djvu',
        'utkandarze_haterlaganda..._vspominaya_proshloe...ofo._2009.djvu': 'utkandarze_haterlaganda..._vspominaya_proshloe...ofo._2009.djvu',
        'bazar_josopova._ofo._1984.djvu': 'bazar_josopova._ofo._1984.djvu',
        'salavat_yulaev._ofo._1994.djvu': 'salavat_yulaev._ofo._1994.djvu',
        'qylys_qynda_kilesha._ofo._2000.djvu': 'qylys_qynda_kilesha._ofo._2000.djvu',
        'başkurt_şecereleri._bashqort_shazharalare._ankara._2009.djvu': 'başkurt_şecereleri._bashqort_shazharalare._ankara._2009.djvu',
        'avtonomiyaly_bashqortostan_bajraghy_astynda._ofo._2009.djvu': 'avtonomiyaly_bashqortostan_bajraghy_astynda._ofo._2009.djvu',
        'kombrig_mortazin_ham_unyng_yauzashtary._ofo._2011.djvu': 'kombrig_mortazin_ham_unyng_yauzashtary._ofo._2011.djvu',
        'bashqortostan_qoshtary._ofo._1986.djvu': 'bashqortostan_qoshtary._ofo._1986.djvu',
        'ilkajem._ofo._2001.djvu': 'ilkajem._ofo._2001.djvu',
        'qaharmandar_yulynan._ofo.1992.djvu': 'qaharmandar_yulynan._ofo.1992.djvu'}
for i in list:
    try:
        os.rename(i, list[i])
    except FileExistsError:
        pass
    except FileNotFoundError:
        pass
    except OSError:
        print(i)