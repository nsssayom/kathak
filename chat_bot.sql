-- Adminer 4.7.1 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

CREATE DATABASE `chat_bot` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `chat_bot`;

DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `alembic_version` (`version_num`) VALUES
('7fbe7589156d');

DROP TABLE IF EXISTS `cart`;
CREATE TABLE `cart` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `is_empty` tinyint(1) NOT NULL,
  `price` float NOT NULL,
  `discount` float NOT NULL,
  `delivery_fee` float NOT NULL,
  `total_price` float NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `cart_item`;
CREATE TABLE `cart_item` (
  `cart_id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL,
  PRIMARY KEY (`cart_id`,`item_id`),
  KEY `item_id` (`item_id`),
  CONSTRAINT `cart_item_ibfk_1` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`id`),
  CONSTRAINT `cart_item_ibfk_2` FOREIGN KEY (`item_id`) REFERENCES `item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `description` varchar(60) NOT NULL,
  `thumb_urls` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `category` (`id`, `name`, `description`, `thumb_urls`) VALUES
(16,	'Food',	'Cheesy food on your doorsteps',	'https://ichef.bbci.co.uk/news/660/cpsprodpb/3DAD/production/_104898751_gettyimages-844466808.jpg'),
(17,	'Cloth',	'Stylish slimfit pants  ',	'https://www.stylist.co.uk/images/app/uploads/2017/06/07164038/shanna-camilleri-190745-unsplash-1400x933.jpg?w=1200&h=1&fit=max&auto=format%2Ccompress'),
(18,	'Electronics',	'Original & modern gadgets for you!',	'https://images.pexels.com/photos/325153/pexels-photo-325153.jpeg?auto=compress&c'),
(19,	'Medicine',	'Life saving medicines',	'https://www.healthnewsreview.org/wp-content/uploads/2018/08/TooMuchMedicine2.jpg'),
(20,	'Cosmetics',	'Original Mac Products!',	'https://img.theculturetrip.com/x/smart/wp-content/uploads/2018/03/cosmetics.jpg');

DROP TABLE IF EXISTS `item`;
CREATE TABLE `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `price` float NOT NULL,
  `description` varchar(60) NOT NULL,
  `cat_id` int(11) DEFAULT NULL,
  `thumb_urls` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `cat_id` (`cat_id`),
  CONSTRAINT `item_ibfk_1` FOREIGN KEY (`cat_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `item` (`id`, `name`, `price`, `description`, `cat_id`, `thumb_urls`) VALUES
(1,	'Burger',	150,	'Juicy and Saucy!',	16,	'https://www.chatelaine.com/wp-content/uploads/2017/05/Bibimbap-homemade-burgers.jpg'),
(2,	'Pizza',	200,	'Crispy and watery Pizza!',	16,	'https://www.lastingredient.com/wp-content/uploads/2013/05/grilled-pizza.jpg'),
(3,	'Sandwich',	100,	'Buttery bread !',	16,	'https://www.bigbasket.com/media/uploads/recipe/w-l/1660_1.jpg'),
(4,	'Pasta',	250,	'Jaw dropping flavor ',	16,	'https://rasamalaysia.com/wp-content/uploads/2018/08/one-pan-pasta-thumb-1.jpg'),
(5,	'Drinks',	100,	'Imported Coca Cola',	16,	'http://www.globalfoods.co.uk/wp-content/uploads/2019/01/61528.jpg'),
(6,	'Kamiz',	800,	'A traditional combination dress worn by women',	17,	'https://cdn.shopify.com/s/files/1/0185/1220/products/32743.jpg?v=1526639925'),
(7,	'Saree',	1200,	'Saree Fabric: Art Silk (5.5 Metres Saree), Blouse Fabric :Ba',	17,	'https://img6.craftsvilla.com/image/upload/w_500/C/V/CV-36102-MCRAF80576334680-1544179443-Craftsvilla_1.jpg'),
(8,	'Shirt',	900,	'Casual stylish shirt',	17,	'https://cdn.shopify.com/s/files/1/0208/0486/2052/products/5b8e5199bb0ab98792751cc2_1024x1024@2x.jpg?v=1558350198'),
(9,	'Mobile',	20000,	'High quality feature phone',	18,	'https://pisces.bbystatic.com/image2/BestBuy_US/images/products/5859/5859415_rd.jpg'),
(10,	'Ipad',	12000,	'Mini Computer ',	18,	'https://store.stormfront.co.uk/content/images/thumbs/0007974_ipad_pureangles_gold_gb-en-screenjpg.jpeg'),
(11,	'Mac Book Pro',	30000,	'Slimmest & Lightest screen ',	18,	'https://cdn.shopify.com/s/files/1/0094/1621/2537/products/BookArc_MacBook2016_Product_530x.jpg?v=1550039420'),
(12,	'Headphone',	2000,	'Enhanced quality headphone',	18,	'https://images-na.ssl-images-amazon.com/images/I/51z376z5iBL._SL1200_.jpg'),
(13,	'Apple Watch',	8000,	'Smart & aesthetic watch',	18,	'https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/44-alu-silver-nike-plat-black-nc-s4-grid?wid=540&hei=550&fmt=jpeg&qlt=80&op_usm=0.5,0.5&.v=1551829304634'),
(14,	'Lipstick',	1500,	'Pinky and glossy ',	20,	'https://images-na.ssl-images-amazon.com/images/I/51tFZ82t8hL._SL1001_.jpg'),
(15,	'Pant',	1700,	'men\'s pants',	17,	'https://rukminim1.flixcart.com/image/880/1056/jevpj0w0/cargo/z/t/a/32-p91-plaindoricargo-plus91-original-imaf3cjyznumzknj.jpeg?q=50'),
(16,	'Eyeliner',	800,	'Black and deep eyeliner',	20,	'https://www.artdeco.com/media/catalog/product/cache/5/image_person/380x/040ec09b1e35df139433887a97daa66f/c/a/calligraphy-dip-eyeliner-artdeco-258101_image_person.jpg'),
(17,	'Baby Dress',	450,	' this is typically made of fabrics or textiles but over',	17,	'https://www.dhresource.com/webp/m/0x0s/f2-albu-g7-M00-E3-15-rBVaSlt7sAaABzpLAAKOwUwkZT4381.jpg/cola-sommer-freizeit-kinder-m-dchen-blumenkleid.jpg'),
(18,	'Nailpolish',	1800,	'Maybeline red nailpolish',	20,	'https://media.allure.com/photos/5d5ec937531caa0008cbc157/master/pass/0820_topcoats_lede_social.jpg'),
(19,	'Perfume',	4000,	'Mildest and Wildest long-lasting odor ',	20,	'https://fimgs.net/mdimg/perfume/375x500.50662.jpg'),
(20,	'Makeup',	2500,	'Wide array of colors',	20,	'https://images-na.ssl-images-amazon.com/images/I/81qKuOti5GL._SL1500_.jpg'),
(21,	'Napa Extra 565mg(10 pcs)',	10,	'Tablet Napa Extra, Generic Name: Caffeine 65 mg + Paracetamo',	19,	'http://officeneeds.com.bd/media/catalog/product/cache/1/thumbnail/600x/d22404af19680639189bc055fa7ef2d2/n/a/napa_extra_epharma_10_pcs_tk25.jpg'),
(22,	'Flexi',	50,	'SQUARE Pharmaceuticals Ltd. the flagship company of Square G',	19,	'http://www.squarepharma.com.bd/products/Flexi.jpg'),
(23,	'Montair',	150,	'Effective lungs tablet ',	19,	'https://5.imimg.com/data5/DN/QX/MY-65309054/montelukast-oral-tablet-500x500.jpg'),
(24,	'Ceevit',	300,	'flavored and tasty ',	19,	'https://biogo.pl/userdata/gfx/36490/cevit-250ml-1.jpg'),
(25,	'Calbo D',	185,	'Brand Name: Calbo D, Manufacturer: Square Pharmaceuticals Li',	19,	'https://www.pharmacy.com.bd/wp-content/uploads/2018/05/Calbo-D-15pcs.jpg');

DROP TABLE IF EXISTS `order`;
CREATE TABLE `order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cart_id` int(11) DEFAULT NULL,
  `Address` varchar(1024) NOT NULL,
  `geo_lat` float NOT NULL,
  `geo_long` float NOT NULL,
  `phone_no` varchar(20) NOT NULL,
  `status` int(11) NOT NULL,
  `placed_on` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cart_id` (`cart_id`),
  CONSTRAINT `order_ibfk_1` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


-- 2019-08-31 06:48:08