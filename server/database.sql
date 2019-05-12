/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50723
Source Host           : localhost:3306
Source Database       : chat

Target Server Type    : MYSQL
Target Server Version : 50723
File Encoding         : 65001

Date: 2019-05-12 14:30:59
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for messages
-- ----------------------------
DROP TABLE IF EXISTS `messages`;
CREATE TABLE `messages` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `author` varchar(64) NOT NULL,
  `text` text NOT NULL,
  `date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of messages
-- ----------------------------
INSERT INTO `messages` VALUES ('4', 'Jeniffer', 'What a lovely day!', '2019-05-09 00:24:42');
INSERT INTO `messages` VALUES ('5', 'John', 'I agree', '2019-05-10 15:20:34');
INSERT INTO `messages` VALUES ('6', 'Mister X', 'It\'s very cold today in the my city :(', '2019-05-10 15:24:55');
INSERT INTO `messages` VALUES ('7', 'John', 'Don\'t worry! We should meet someday', '2019-05-12 00:26:58');
SET FOREIGN_KEY_CHECKS=1;
