PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE cfp_class (
        class_id TEXT PRIMARY KEY,
        class_name TEXT
    );
INSERT INTO cfp_class VALUES('c1','能源類');
INSERT INTO cfp_class VALUES('c2','材料類');
INSERT INTO cfp_class VALUES('c3','食品類');
INSERT INTO cfp_class VALUES('c4','服務類');
INSERT INTO cfp_class VALUES('c5','其他');
CREATE TABLE cfp_sub_class (
        sub_class_id TEXT PRIMARY KEY,
        sub_class_name TEXT,
        class_id TEXT,
        FOREIGN KEY (class_id) REFERENCES cfp_class(class_id)
    );
CREATE TABLE cfp_sos_class (
        cfp_sos_class_id TEXT PRIMARY KEY,
        cfp_sos_class_name TEXT,
        cfp_sub_class_id TEXT,
        FOREIGN KEY (cfp_sub_class_id) REFERENCES cfp_sub_class(sub_class_id)
    );
CREATE TABLE summer_c2_rates (
        h_id INTEGER PRIMARY KEY AUTOINCREMENT,
        wday_rate TEXT REFERENCES time_elec_rates(desc),
        wend_rate TEXT REFERENCES time_elec_rates(desc)
    );
INSERT INTO summer_c2_rates VALUES(0,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(1,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(2,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(3,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(4,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(5,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(6,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(7,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(8,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(9,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(10,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(11,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(12,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(13,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(14,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(15,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(16,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(17,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(18,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(19,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(20,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(21,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(22,'summ_peak_cat2','summer_off_peak');
INSERT INTO summer_c2_rates VALUES(23,'summ_peak_cat2','summer_off_peak');
CREATE TABLE c2_rates (
        h_id INTEGER PRIMARY KEY AUTOINCREMENT,
        wday_rate TEXT REFERENCES time_elec_rates(desc),
        wend_rate TEXT REFERENCES time_elec_rates(desc)
    );
INSERT INTO c2_rates VALUES(0,'off_peak','off_peak');
INSERT INTO c2_rates VALUES(1,'off_peak','off_peak');
INSERT INTO c2_rates VALUES(2,'off_peak','off_peak');
INSERT INTO c2_rates VALUES(3,'off_peak','off_peak');
INSERT INTO c2_rates VALUES(4,'off_peak','off_peak');
INSERT INTO c2_rates VALUES(5,'off_peak','off_peak');
INSERT INTO c2_rates VALUES(6,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(7,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(8,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(9,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(10,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(11,'off_peak','off_peak');
INSERT INTO c2_rates VALUES(12,'off_peak','off_peak');
INSERT INTO c2_rates VALUES(13,'off_peak','off_peak');
INSERT INTO c2_rates VALUES(14,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(15,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(16,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(17,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(18,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(19,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(20,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(21,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(22,'peak_cat2','off_peak');
INSERT INTO c2_rates VALUES(23,'peak_cat2','off_peak');
CREATE TABLE summer_c3_rates (
        h_id INTEGER PRIMARY KEY AUTOINCREMENT,
        wday_rate TEXT REFERENCES time_elec_rates(desc),
        wend_rate TEXT REFERENCES time_elec_rates(desc)
    );
INSERT INTO summer_c3_rates VALUES(0,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(1,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(2,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(3,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(4,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(5,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(6,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(7,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(8,'summer_off_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(9,'summ_semi_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(10,'summ_semi_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(11,'summ_semi_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(12,'summ_semi_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(13,'summ_semi_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(14,'summ_semi_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(15,'summ_semi_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(16,'summ_peak_cat3','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(17,'summ_peak_cat3','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(18,'summ_peak_cat3','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(19,'summ_peak_cat3','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(20,'summ_peak_cat3','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(21,'summ_peak_cat3','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(22,'summ_semi_peak','summer_off_peak');
INSERT INTO summer_c3_rates VALUES(23,'summ_semi_peak','summer_off_peak');
CREATE TABLE c3_rates (
        h_id INTEGER PRIMARY KEY AUTOINCREMENT,
        wday_rate TEXT REFERENCES time_elec_rates(desc),
        wend_rate TEXT REFERENCES time_elec_rates(desc)
    );
INSERT INTO c3_rates VALUES(0,'off_peak','off_peak');
INSERT INTO c3_rates VALUES(1,'off_peak','off_peak');
INSERT INTO c3_rates VALUES(2,'off_peak','off_peak');
INSERT INTO c3_rates VALUES(3,'off_peak','off_peak');
INSERT INTO c3_rates VALUES(4,'off_peak','off_peak');
INSERT INTO c3_rates VALUES(5,'off_peak','off_peak');
INSERT INTO c3_rates VALUES(6,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(7,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(8,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(9,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(10,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(11,'off_peak','off_peak');
INSERT INTO c3_rates VALUES(12,'off_peak','off_peak');
INSERT INTO c3_rates VALUES(13,'off_peak','off_peak');
INSERT INTO c3_rates VALUES(14,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(15,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(16,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(17,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(18,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(19,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(20,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(21,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(22,'semi_peak','off_peak');
INSERT INTO c3_rates VALUES(23,'semi_peak','off_peak');
CREATE TABLE IF NOT EXISTS "time_elec_rates" (
    desc TEXT,
    effect_date INTEGER,
    rates REAL,
    PRIMARY KEY (desc, effect_date)
);
INSERT INTO time_elec_rates VALUES('off_peak',11204,1.780000000000000071);
INSERT INTO time_elec_rates VALUES('summer_off_peak',11204,1.85);
INSERT INTO time_elec_rates VALUES('semi_peak',11204,4.0599999999999996092);
INSERT INTO time_elec_rates VALUES('summ_semi_peak',11204,4.2599999999999997868);
INSERT INTO time_elec_rates VALUES('peak_cat2',11204,4.4800000000000004263);
INSERT INTO time_elec_rates VALUES('summ_peak_cat2',11204,4.7099999999999999644);
INSERT INTO time_elec_rates VALUES('peak_cat3',11204,0.0);
INSERT INTO time_elec_rates VALUES('summ_peak_cat3',11204,6.4900000000000002131);
INSERT INTO time_elec_rates VALUES('over_rate',11204,0.99000000000000003552);
CREATE TABLE beverage (
        id TEXT PRIMARY KEY,
        name TEXT,
        cde REAL,
        unit TEXT,
        UNIQUE(name, unit) -- Define a unique key constraint on name and unit
    );
INSERT INTO beverage VALUES('c3s09i001','58度特級高粱酒，600ml',4.0,'瓶');
INSERT INTO beverage VALUES('c3s09i002','高粱酒（50%，600ml）',5.5,'瓶');
INSERT INTO beverage VALUES('c3s09i003','經典台灣啤酒，330 ml (6罐裝，收縮膜)',0.21000000000000000888,'罐');
INSERT INTO beverage VALUES('c3s09i004','經典台灣啤酒，330 ml (6罐裝，收縮膜)',1.2900000000000000355,'組');
INSERT INTO beverage VALUES('c3s09i005','經典台灣啤酒，330 ml (24罐裝，紙箱)',0.21000000000000000888,'罐');
INSERT INTO beverage VALUES('c3s09i006','經典台灣啤酒，330 ml (24罐裝，紙箱)',5.1399999999999996802,'箱');
INSERT INTO beverage VALUES('c3s09i007','經典台灣啤酒，500 ml (24罐裝，紙箱)',0.32000000000000001776,'罐');
INSERT INTO beverage VALUES('c3s09i008','經典台灣啤酒，500 ml (24罐裝，紙箱)',7.6399999999999996802,'箱');
INSERT INTO beverage VALUES('c3s09i009','經典台灣啤酒，600 ml (玻璃瓶裝)',0.33000000000000002664,'瓶');
INSERT INTO beverage VALUES('c3s09i010','金牌台灣啤酒，330 ml (6罐裝，收縮膜)',0.22000000000000001776,'罐');
INSERT INTO beverage VALUES('c3s09i011','金牌台灣啤酒，330 ml (6罐裝，收縮膜)',1.330000000000000071,'組');
INSERT INTO beverage VALUES('c3s09i012','金牌台灣啤酒，330 ml (24罐裝，紙箱)',0.22000000000000001776,'罐');
INSERT INTO beverage VALUES('c3s09i013','金牌台灣啤酒，330 ml (24罐裝，紙箱)',5.2999999999999998223,'箱');
INSERT INTO beverage VALUES('c3s09i014','金牌台灣啤酒，500 ml (24罐裝，紙箱)',0.33000000000000002664,'罐');
INSERT INTO beverage VALUES('c3s09i015','金牌台灣啤酒，500 ml (24罐裝，紙箱)',7.8799999999999998934,'箱');
INSERT INTO beverage VALUES('c3s09i016','金牌台灣啤酒，600 ml (12瓶裝，紙箱)',0.4,'瓶');
INSERT INTO beverage VALUES('c3s09i017','金牌台灣啤酒，600 ml (12瓶裝，紙箱)',9.4800000000000004263,'箱');
INSERT INTO beverage VALUES('c3s09i018','豆漿，450ml(鋁箔包裝)',0.16000000000000000888,'盒');
INSERT INTO beverage VALUES('c3s09i019','豆漿（450ml，鋁箔包裝）',0.37999999999999998223,'盒');
INSERT INTO beverage VALUES('c3s09i020','紅茶，250ml(鋁箔包裝)',0.095,'包');
INSERT INTO beverage VALUES('c3s09i021','紅茶，300ml(鋁箔包裝)',0.11000000000000000888,'包');
INSERT INTO beverage VALUES('c3s09i022','紅茶，375ml(鋁箔包裝)',0.13000000000000000444,'包');
INSERT INTO beverage VALUES('c3s09i023','紅茶',7.0400000000000000355,'公斤(kg)');
INSERT INTO beverage VALUES('c3s09i024','紅茶（250ml，鋁箔包裝）',0.1,'包');
INSERT INTO beverage VALUES('c3s09i025','紅茶（300ml，鋁箔包裝）',0.11999999999999999644,'包');
INSERT INTO beverage VALUES('c3s09i026','紅茶（375ml，鋁箔包裝）',0.16000000000000000888,'包');
INSERT INTO beverage VALUES('c3s09i027','奶茶，250ml(鋁箔包裝)',0.11000000000000000888,'包');
INSERT INTO beverage VALUES('c3s09i028','奶茶，300ml(鋁箔包裝)',0.13000000000000000444,'包');
INSERT INTO beverage VALUES('c3s09i029','奶茶，375ml(鋁箔包裝)',0.16000000000000000888,'包');
INSERT INTO beverage VALUES('c3s09i030','奶茶（250ml，鋁箔包裝）',0.13000000000000000444,'包');
INSERT INTO beverage VALUES('c3s09i031','奶茶（300ml，鋁箔包裝）',0.14000000000000001776,'包');
INSERT INTO beverage VALUES('c3s09i032','奶茶（375ml，鋁箔包裝）',0.2,'包');
INSERT INTO beverage VALUES('c3s09i033','綠茶，250ml(鋁箔包裝)',0.09,'包');
INSERT INTO beverage VALUES('c3s09i034','綠茶，300ml(鋁箔包裝)',0.1,'包');
INSERT INTO beverage VALUES('c3s09i035','綠茶（250ml，鋁箔包裝）',0.11000000000000000888,'包');
INSERT INTO beverage VALUES('c3s09i036','綠茶（300ml，鋁箔包裝）',0.11999999999999999644,'包');
INSERT INTO beverage VALUES('c3s09i037','高山烏龍茶(無烘培-部分發酵)',5.7099999999999999644,'包');
INSERT INTO beverage VALUES('c3s09i038','高山烏龍茶(有烘培-部分發酵)',7.6900000000000003907,'包');
INSERT INTO beverage VALUES('c3s09i039','高山烏龍茶(無烘培-完全發酵)',6.2999999999999998223,'包');
INSERT INTO beverage VALUES('c3s09i040','精力湯',3.4700000000000001953,'包');
INSERT INTO beverage VALUES('c3s09i041','擂茶',3.6400000000000001243,'包');
INSERT INTO beverage VALUES('c3s09i042','可樂(寶特瓶裝，600ml)',0.39800000000000004263,'瓶');
INSERT INTO beverage VALUES('c3s09i043','可樂(寶特瓶裝，2L)',0.64400000000000003907,'瓶');
INSERT INTO beverage VALUES('c3s09i044','柳橙汁(450ml)',0.25400000000000000355,'瓶');
INSERT INTO beverage VALUES('c3s09i045','瓶裝水（600ml，PET包裝）',0.1530000000000000071,'瓶');
INSERT INTO beverage VALUES('c3s09i046','瓶裝水（1500ml，PET包裝）',0.25,'瓶');
INSERT INTO beverage VALUES('c3s09i047','瓶裝水（2000ml，PET包裝）',0.36799999999999997157,'瓶');
INSERT INTO beverage VALUES('c3s09i048','瓶裝水(330ml，PET包裝) ',0.15,'瓶');
INSERT INTO beverage VALUES('c3s09i049','瓶裝水(600ml，PET包裝)',0.14000000000000001776,'瓶');
INSERT INTO beverage VALUES('c3s09i050','瓶裝水(1500ml，PET包裝)',0.27000000000000001776,'瓶');
INSERT INTO beverage VALUES('c3s09i051','包裝飲用水(600ml，PET包裝)',0.12099999999999999644,'瓶');
INSERT INTO beverage VALUES('c3s09i052','包裝飲用水(1460ml，PET包裝)',0.25300000000000002486,'瓶');
CREATE TABLE egg_prods (
        id TEXT PRIMARY KEY,
        name TEXT,
        cde REAL,
        unit TEXT,
        UNIQUE(name, unit) -- Define a unique key constraint on name and unit
    );
INSERT INTO egg_prods VALUES('c3s05i001','紅殼雞蛋',0.10700000000000000621,'顆');
INSERT INTO egg_prods VALUES('c3s05i002','雞蛋',0.16200000000000001065,'顆');
INSERT INTO egg_prods VALUES('c3s05i003','PLA蛋盤(10盒裝)',4.7800000000000002486,'公斤(kg)');
INSERT INTO egg_prods VALUES('c3s05i004','茶葉蛋',2.3999999999999999111,'包');
INSERT INTO egg_prods VALUES('c3s05i005','鮮蛋',0.10500000000000000444,'顆');
CREATE TABLE lactose_prods (
        id TEXT PRIMARY KEY,
        name TEXT,
        cde REAL,
        unit TEXT,
        UNIQUE(name, unit) -- Define a unique key constraint on name and unit
    );
INSERT INTO lactose_prods VALUES('c3s08i001','鮮乳',2.4799999999999999822,'公升(L)');
INSERT INTO lactose_prods VALUES('c3s08i002','麥芽調味乳',3.3100000000000000532,'公升(L)');
INSERT INTO lactose_prods VALUES('c3s08i003','焦糖烤布丁',0.34000000000000003552,'個');
INSERT INTO lactose_prods VALUES('c3s08i004','凝乳塊(未發酵)',12.399999999999999911,'公斤(kg)');
INSERT INTO lactose_prods VALUES('c3s08i005','優酪乳',1.95,'公斤(kg)');
INSERT INTO lactose_prods VALUES('c3s08i006','優格',4.330000000000000071,'公斤(kg)');
CREATE TABLE energy (
        id TEXT PRIMARY KEY,
        name TEXT,
        cde REAL,
        unit TEXT,
        UNIQUE(name, unit) -- Define a unique key constraint on name and unit
    );
INSERT INTO energy VALUES('c1s01i001','液化天然氣(於固定源使用，2012)',2.5200000000000000177,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i002','液化石油氣(於固定源使用，2012)',2.0899999999999998578,'公升(L)');
INSERT INTO energy VALUES('c1s01i003','液化天然氣(於固定源使用，2013)',2.5899999999999998578,'立方公尺m3');
INSERT INTO energy VALUES('c1s01i004','液化石油氣(於固定源使用，2013)',2.3399999999999998578,'公升(L)');
INSERT INTO energy VALUES('c1s01i005','液化天然氣(於固定源使用，2014)',2.6099999999999998756,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i006','液化石油氣(於固定源使用，2014)',2.2599999999999997868,'公升(L)');
INSERT INTO energy VALUES('c1s01i007','天然氣(於固定源使用，2015)',2.6099999999999998756,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i008','液化石油氣(於固定源使用，2015)',2.2599999999999997868,'公升(L)');
INSERT INTO energy VALUES('c1s01i009','天然氣(於固定源使用，2016)',2.6000000000000000888,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i010','液化石油氣(於固定源使用，2016)',2.2400000000000002131,'公升(L)');
INSERT INTO energy VALUES('c1s01i011','液化天然氣（未燃燒，韓國，2006）',0.59499999999999992894,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i012','液化石油氣（未燃燒，韓國，2006）',0.39400000000000003907,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i013','液化石油氣（未燃燒，泰國，2008）',0.41200000000000001065,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i014','天然氣(於固定源使用，2017)',2.6000000000000000888,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i015','液化石油氣(於固定源使用，2017)',2.25,'公升(L)');
INSERT INTO energy VALUES('c1s01i016','天然氣(於固定源使用，2018)',2.580000000000000071,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i017','天然氣(未燃燒，2018)',0.46899999999999995026,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i018','液化石油氣(於固定源使用，2018)',2.25,'公升(L)');
INSERT INTO energy VALUES('c1s01i019','液化石油氣(未燃燒，2018)',0.49100000000000001421,'公升(L)');
INSERT INTO energy VALUES('c1s01i020','天然氣(於固定源使用，2019)',2.5600000000000000532,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i021','天然氣(未燃燒，2019)',0.45099999999999997868,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i022','液化石油氣(於固定源使用，2019)',2.2200000000000001953,'公升(L)');
INSERT INTO energy VALUES('c1s01i023','液化石油氣(未燃燒，2019)',0.46699999999999999289,'公升(L)');
INSERT INTO energy VALUES('c1s01i024','天然氣(於固定源使用，2020)',2.6299999999999998934,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i025','天然氣(未燃燒，2020)',0.51600000000000001421,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i026','液化石油氣(於固定源使用，2020)',2.2200000000000001953,'公升(L)');
INSERT INTO energy VALUES('c1s01i027','液化石油氣(未燃燒，2020)',0.46699999999999999289,'公升(L)');
INSERT INTO energy VALUES('c1s01i028','台灣自來水 (2011)',0.16700000000000001065,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i029','臺北自來水 (2013)',0.17000000000000001776,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i030','臺灣自來水(2017)',0.29899999999999998578,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i031','臺灣自來水(2020)',0.2330000000000000071,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i032','臺北自來水(2020)',0.094800000000000004263,'立方公尺(m3)');
INSERT INTO energy VALUES('c1s01i033','燃料油使用(蒸餘油/重油使用，2012)',3.980000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i034','柴油(未燃燒，2012)',0.74000000000000003552,'公升(L)');
INSERT INTO energy VALUES('c1s01i035','柴油(於固定源使用，2012)',3.4199999999999999289,'公升(L)');
INSERT INTO energy VALUES('c1s01i036','柴油(於移動源使用，2012年)',3.4500000000000001776,'公升(L)');
INSERT INTO energy VALUES('c1s01i037','車用汽油(未燃燒，2012)',0.65,'公升(L)');
INSERT INTO energy VALUES('c1s01i038','車用汽油(於固定源使用，2012)',3.0,'公升(L)');
INSERT INTO energy VALUES('c1s01i039','車用汽油(於移動源使用，2012)',3.1000000000000000888,'公升(L)');
INSERT INTO energy VALUES('c1s01i040','燃料油使用(蒸餘油/重油使用，2013)',4.0199999999999995736,'公升(L)');
INSERT INTO energy VALUES('c1s01i041','柴油(未燃燒，2013)',0.75999999999999996447,'公升(L)');
INSERT INTO energy VALUES('c1s01i042','柴油(於固定源使用，2013)',3.4599999999999999644,'公升(L)');
INSERT INTO energy VALUES('c1s01i043','柴油(於移動源使用，2013)',3.4900000000000002131,'公升(L)');
INSERT INTO energy VALUES('c1s01i044','車用汽油(未燃燒，2013)',0.6899999999999999467,'公升(L)');
INSERT INTO energy VALUES('c1s01i045','車用汽油(於固定源使用，2013)',3.0299999999999998046,'公升(L)');
INSERT INTO energy VALUES('c1s01i046','車用汽油(於移動源使用，2013)',3.1200000000000001065,'公升(L)');
INSERT INTO energy VALUES('c1s01i047','燃料油使用(蒸餘油/重油使用，2014)',4.0,'公升(L)');
INSERT INTO energy VALUES('c1s01i048','柴油(未燃燒，2014)',0.75,'公升(L)');
INSERT INTO energy VALUES('c1s01i049','柴油(於固定源使用，2014)',3.4500000000000001776,'公升(L)');
INSERT INTO energy VALUES('c1s01i050','柴油(於移動源使用，2014)',3.4799999999999999822,'公升(L)');
INSERT INTO energy VALUES('c1s01i051','車用汽油(未燃燒，2014)',0.67000000000000001776,'公升(L)');
INSERT INTO energy VALUES('c1s01i052','車用汽油(於固定源使用，2014)',3.0200000000000000177,'公升(L)');
INSERT INTO energy VALUES('c1s01i053','車用汽油(於移動源使用，2014)',3.1000000000000000888,'公升(L)');
INSERT INTO energy VALUES('c1s01i054','煤油使用(2014)',3.0200000000000000177,'公升(L)');
INSERT INTO energy VALUES('c1s01i055','燃料油使用(蒸餘油/重油使用，2015)',4.0,'公升(L)');
INSERT INTO energy VALUES('c1s01i056','柴油(未燃燒，2015)',0.75199999999999995736,'公升(L)');
INSERT INTO energy VALUES('c1s01i057','柴油(於固定源使用，2015)',3.4500000000000001776,'公升(L)');
INSERT INTO energy VALUES('c1s01i058','柴油(於移動源使用，2015)',3.4799999999999999822,'公升(L)');
INSERT INTO energy VALUES('c1s01i059','車用汽油(未燃燒，2015)',0.67100000000000008526,'公升(L)');
INSERT INTO energy VALUES('c1s01i060','車用汽油(於固定源使用，2015)',3.0200000000000000177,'公升(L)');
INSERT INTO energy VALUES('c1s01i061','車用汽油(於移動源使用，2015)',3.1000000000000000888,'公升(L)');
INSERT INTO energy VALUES('c1s01i062','煤油使用(2015)',3.0200000000000000177,'公升(L)');
INSERT INTO energy VALUES('c1s01i063','生質燃料油使用(含10%低硫燃料油，2015)',3140.0,'公秉(kl)');
INSERT INTO energy VALUES('c1s01i064','燃料油使用(蒸餘油/重油使用，2016)',3.9599999999999999644,'公升(L)');
INSERT INTO energy VALUES('c1s01i065','柴油(未燃燒，2016)',0.73499999999999996447,'公升(L)');
INSERT INTO energy VALUES('c1s01i066','柴油(於固定源使用，2016)',3.3500000000000000888,'公升(L)');
INSERT INTO energy VALUES('c1s01i067','柴油(於公路運輸移動源使用，2016)',3.3799999999999998934,'公升(L)');
INSERT INTO energy VALUES('c1s01i068','車用汽油(未燃燒，2016)',0.65600000000000004973,'公升(L)');
INSERT INTO energy VALUES('c1s01i069','車用汽油(於固定源使用，2016)',2.930000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i070','車用汽油(於移動源使用，2016)',3.0099999999999997868,'公升(L)');
INSERT INTO energy VALUES('c1s01i071','煤油使用(2016)',2.980000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i072','柴油（於鐵路運輸與非道路運輸移動源使用，2016）',3.6099999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i073','柴油（於水路運輸移動源使用，2016）',3.3700000000000001065,'公升(L)');
INSERT INTO energy VALUES('c1s01i074','柴油（於捕撈移動源使用，2016）',3.3599999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i075','柴油（未燃燒，韓國，2000）',0.06819999999999999396,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i076','重質燃料油（未燃燒，韓國，1998）',0.325,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i077','汽油（未燃燒，韓國，2000）',0.083200000000000002842,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i078','汽油（未燃燒，泰國，2005）',0.70599999999999996092,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i079','燃料油（未燃燒，泰國，2005）',0.30499999999999998223,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i080','柴油（未燃燒，泰國，2005）',0.32800000000000002486,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i081','燃料油使用(蒸餘油/重油使用，2017)',3.9599999999999999644,'公升(L)');
INSERT INTO energy VALUES('c1s01i082','柴油(未燃燒，2017)',0.73499999999999996447,'公升(L)');
INSERT INTO energy VALUES('c1s01i083','柴油(於固定源使用，2017)',3.3500000000000000888,'公升(L)');
INSERT INTO energy VALUES('c1s01i084','柴油(於公路運輸移動源使用，2017)',3.3799999999999998934,'公升(L)');
INSERT INTO energy VALUES('c1s01i085','柴油(於鐵路運輸與非道路運輸移動源使用，2017)',3.6099999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i086','柴油(於水路運輸移動源使用，2017)',3.3700000000000001065,'公升(L)');
INSERT INTO energy VALUES('c1s01i087','柴油(於捕撈移動源使用，2017)',3.3599999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i088','車用汽油(未燃燒，2017)',0.6580000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i089','車用汽油(於固定源使用，2017)',2.930000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i090','車用汽油(於移動源使用，2017)',3.0200000000000000177,'公升(L)');
INSERT INTO energy VALUES('c1s01i091','煤油使用(2017)',2.980000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i092','潤滑油（未燃燒，2017）',1.0500000000000000444,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i093','燃料油使用(蒸餘油/重油使用，2018)',3.9399999999999998578,'公升(L)');
INSERT INTO energy VALUES('c1s01i094','燃料油未燃燒(蒸餘油/重油未燃燒，2018)',0.82199999999999988631,'公升(L)');
INSERT INTO energy VALUES('c1s01i095','柴油(未燃燒，2018)',0.72400000000000002131,'公升(L)');
INSERT INTO energy VALUES('c1s01i096','柴油(於固定源使用，2018)',3.3399999999999998578,'公升(L)');
INSERT INTO energy VALUES('c1s01i097','柴油(於公路運輸移動源使用，2018)',3.3700000000000001065,'公升(L)');
INSERT INTO energy VALUES('c1s01i098','柴油(於鐵路運輸與非道路運輸移動源使用，2018)',3.6000000000000000888,'公升(L)');
INSERT INTO energy VALUES('c1s01i099','柴油(於水路運輸移動源使用，2018)',3.3599999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i100','柴油(於捕撈移動源使用，2018)',3.3500000000000000888,'公升(L)');
INSERT INTO energy VALUES('c1s01i101','車用汽油(未燃燒，2018)',0.65,'公升(L)');
INSERT INTO energy VALUES('c1s01i102','車用汽油(於固定源使用，2018)',2.9199999999999999289,'公升(L)');
INSERT INTO energy VALUES('c1s01i103','車用汽油(於移動源使用，2018)',3.0099999999999997868,'公升(L)');
INSERT INTO energy VALUES('c1s01i104','煤油使用(2018)',2.9700000000000002842,'公升(L)');
INSERT INTO energy VALUES('c1s01i105','煤油(未燃燒，2018)',0.40300000000000002486,'公升(L)');
INSERT INTO energy VALUES('c1s01i106','潤滑油（未燃燒，2018）',1.0200000000000000177,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i107','燃料油使用(蒸餘油/重油使用，2019)',3.9500000000000001776,'公升(L)');
INSERT INTO energy VALUES('c1s01i108','燃料油未燃燒(蒸餘油/重油未燃燒，2019)',0.83200000000000002842,'公升(L)');
INSERT INTO energy VALUES('c1s01i109','柴油(未燃燒，2019)',0.7330000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i110','柴油(於固定源使用，2019)',3.3500000000000000888,'公升(L)');
INSERT INTO energy VALUES('c1s01i111','柴油(於公路運輸移動源使用，2019)',3.3799999999999998934,'公升(L)');
INSERT INTO energy VALUES('c1s01i112','柴油(於鐵路運輸與非道路運輸移動源使用，2019)',3.6099999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i113','柴油(於水路運輸移動源使用，2019)',3.3599999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i114','柴油(於捕撈移動源使用，2019)',3.3599999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i115','車用汽油(未燃燒，2019)',0.66000000000000005329,'公升(L)');
INSERT INTO energy VALUES('c1s01i116','車用汽油(於固定源使用，2019)',2.930000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i117','車用汽油(於移動源使用，2019)',3.0200000000000000177,'公升(L)');
INSERT INTO energy VALUES('c1s01i118','煤油使用(2019)',2.980000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i119','煤油(未燃燒，2019)',0.41299999999999998934,'公升(L)');
INSERT INTO energy VALUES('c1s01i120','潤滑油（未燃燒，2019）',1.0200000000000000177,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i121','燃料油使用(蒸餘油/重油使用，2020)',3.9500000000000001776,'公升(L)');
INSERT INTO energy VALUES('c1s01i122','燃料油未燃燒(蒸餘油/重油未燃燒，2020)',0.82899999999999991473,'公升(L)');
INSERT INTO energy VALUES('c1s01i123','柴油(未燃燒，2020)',0.72999999999999998223,'公升(L)');
INSERT INTO energy VALUES('c1s01i124','柴油(於固定源使用，2020)',3.3399999999999998578,'公升(L)');
INSERT INTO energy VALUES('c1s01i125','柴油(於公路運輸移動源使用，2020)',3.3799999999999998934,'公升(L)');
INSERT INTO energy VALUES('c1s01i126','柴油(於鐵路運輸與非道路運輸移動源使用，2020)',3.6099999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i127','柴油(於水路運輸移動源使用，2020)',3.3599999999999998756,'公升(L)');
INSERT INTO energy VALUES('c1s01i128','柴油(於捕撈移動源使用，2020)',3.3500000000000000888,'公升(L)');
INSERT INTO energy VALUES('c1s01i129','車用汽油(未燃燒，2020)',0.65700000000000002842,'公升(L)');
INSERT INTO energy VALUES('c1s01i130','車用汽油(於固定源使用，2020)',2.930000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i131','車用汽油(於移動源使用，2020)',3.0099999999999997868,'公升(L)');
INSERT INTO energy VALUES('c1s01i132','煤油使用(2020)',2.980000000000000071,'公升(L)');
INSERT INTO energy VALUES('c1s01i133','煤油(未燃燒，2020)',0.41099999999999994315,'公升(L)');
INSERT INTO energy VALUES('c1s01i134','潤滑油（未燃燒，2020）',1.090000000000000071,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i135','電(2020）',0.5330000000000000071,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i136','電(2021）',0.50899999999999998578,'公斤(kg)');
INSERT INTO energy VALUES('c1s01i137','電(2022）',0.49500000000000001776,'公斤(kg)');
CREATE TABLE elec_device_consumption (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        watt INTEGER,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
INSERT INTO elec_device_consumption VALUES(1,'電冰箱',130,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(2,'電鍋',800,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(3,'開飲機',800,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(4,'微波爐',1200,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(5,'抽油煙機',350,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(6,'果汁機',210,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(7,'果榨汁機',410,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(8,'烘碗機',200,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(9,'電磁爐',1200,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(10,'多功能火鍋',1350,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(11,'烤麵包機',900,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(12,'電咖啡壺',590,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(13,'電烤箱',800,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(14,'洗衣機',420,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(15,'乾衣機',1200,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(16,'電熨斗',800,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(17,'冷氣機',900,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(18,'吹風機',800,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(19,'電暖爐',700,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(20,'除濕機',285,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(21,'電扇',66,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(22,'吸塵器',400,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(23,'抽風機',30,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(24,'燈泡(60W)',60,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(25,'日光燈(20W)',25,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(26,'省電燈泡',17,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(27,'神龕燈',10,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(28,'電視機',140,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(29,'機上盒',15,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(30,'音響',50,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(31,'收音機',10,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(32,'電腦:主機+顯示器',370,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(33,'印表機',12,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(34,'手機充電器',15,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(35,'筆記型電腦MacBook Pro',85,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(36,'電熱水器',6000,'2023-09-08 23:30:41');
INSERT INTO elec_device_consumption VALUES(37,'電熱水瓶',950,'2023-09-09 15:15:54');
INSERT INTO elec_device_consumption VALUES(38,'變頻冷氣',450,'2023-09-10 15:40:49');
CREATE TABLE cde_transport (
        id TEXT PRIMARY KEY,
        name TEXT,
        cde REAL,
        unit TEXT,
        UNIQUE(name, unit) -- Define a unique key constraint on name and unit
    );
INSERT INTO cde_transport VALUES('c4s01i001','自用小客車(汽油) ',0.11500000000000001332,'延人公里(pkm)');
INSERT INTO cde_transport VALUES('c4s01i002','營業小客車(汽油) ',0.1330000000000000071,'延人公里(pkm)');
INSERT INTO cde_transport VALUES('c4s01i003','自用小貨車(汽油) ',0.73899999999999996802,'延頓公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i004','自用小貨車(柴油) ',0.69299999999999997157,'延頓公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i005','營業小貨車(汽油) ',0.62599999999999997868,'延頓公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i006','營業小貨車(柴油) ',0.64700000000000006394,'延頓公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i007','自用大客車(柴油)',0.060599999999999996092,'延人公里(pkm)');
INSERT INTO cde_transport VALUES('c4s01i008','營業遊覽車(柴油) ',0.044100000000000001421,'延人公里(pkm)');
INSERT INTO cde_transport VALUES('c4s01i009','營業大客車(市區公車及公路客運-柴油) ',0.094399999999999995026,'延人公里(pkm)');
INSERT INTO cde_transport VALUES('c4s01i010','自用大貨車(柴油) ',0.22400000000000002131,'延頓公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i011','營業大貨車(柴油) ',0.23499999999999996447,'延頓公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i012','機器腳踏車(汽油) ',0.095100000000000015631,'延人公里(pkm)');
INSERT INTO cde_transport VALUES('c4s01i013','國內海運-貨運，柴油動力',0.033399999999999998578,'延頓公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i014','國際海運-貨運，燃料油動力',0.035400000000000000355,'延頓公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i015','國內海運-貨運，燃料油動力',0.01980000000000000071,'延頓公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i016','營業大貨車(柴油)',0.13100000000000000532,'延噸公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i017','營業小貨車(柴油)',0.58699999999999992184,'延噸公里(tkm)');
INSERT INTO cde_transport VALUES('c4s01i018','營業小貨車(汽油)',0.6830000000000000071,'延噸公里(tkm)');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('summer_c2_rates',24);
INSERT INTO sqlite_sequence VALUES('c2_rates',24);
INSERT INTO sqlite_sequence VALUES('c3_rates',24);
INSERT INTO sqlite_sequence VALUES('summer_c3_rates',24);
INSERT INTO sqlite_sequence VALUES('elec_device_consumption',38);
CREATE TRIGGER generate_class_id
    BEFORE INSERT ON cfp_class
    BEGIN
        INSERT INTO cfp_class (class_id, class_name) 
        VALUES (
            'c' || (SELECT COALESCE(MAX(CAST(SUBSTR(class_id, 2) AS INTEGER)), 0) + 1 FROM cfp_class),
            NEW.class_name
        );
    END;
COMMIT;
