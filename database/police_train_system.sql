/*
 Navicat MySQL Data Transfer

 Source Server         : remote
 Source Server Type    : MySQL
 Source Server Version : 80025
 Source Host           : 39.105.139.161:3306
 Source Schema         : police_train_system

 Target Server Type    : MySQL
 Target Server Version : 80025
 File Encoding         : 65001

 Date: 06/09/2021 11:08:12
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `name`(`name`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_group_permissions_group_id_permission_id_0cd325b0_uniq`(`group_id`, `permission_id`) USING BTREE,
  INDEX `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `auth_permission_content_type_id_codename_01ab375a_uniq`(`content_type_id`, `codename`) USING BTREE,
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 65 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES (1, 'Can add log entry', 1, 'add_logentry');
INSERT INTO `auth_permission` VALUES (2, 'Can change log entry', 1, 'change_logentry');
INSERT INTO `auth_permission` VALUES (3, 'Can delete log entry', 1, 'delete_logentry');
INSERT INTO `auth_permission` VALUES (4, 'Can view log entry', 1, 'view_logentry');
INSERT INTO `auth_permission` VALUES (5, 'Can add permission', 2, 'add_permission');
INSERT INTO `auth_permission` VALUES (6, 'Can change permission', 2, 'change_permission');
INSERT INTO `auth_permission` VALUES (7, 'Can delete permission', 2, 'delete_permission');
INSERT INTO `auth_permission` VALUES (8, 'Can view permission', 2, 'view_permission');
INSERT INTO `auth_permission` VALUES (9, 'Can add group', 3, 'add_group');
INSERT INTO `auth_permission` VALUES (10, 'Can change group', 3, 'change_group');
INSERT INTO `auth_permission` VALUES (11, 'Can delete group', 3, 'delete_group');
INSERT INTO `auth_permission` VALUES (12, 'Can view group', 3, 'view_group');
INSERT INTO `auth_permission` VALUES (13, 'Can add content type', 4, 'add_contenttype');
INSERT INTO `auth_permission` VALUES (14, 'Can change content type', 4, 'change_contenttype');
INSERT INTO `auth_permission` VALUES (15, 'Can delete content type', 4, 'delete_contenttype');
INSERT INTO `auth_permission` VALUES (16, 'Can view content type', 4, 'view_contenttype');
INSERT INTO `auth_permission` VALUES (17, 'Can add session', 5, 'add_session');
INSERT INTO `auth_permission` VALUES (18, 'Can change session', 5, 'change_session');
INSERT INTO `auth_permission` VALUES (19, 'Can delete session', 5, 'delete_session');
INSERT INTO `auth_permission` VALUES (20, 'Can view session', 5, 'view_session');
INSERT INTO `auth_permission` VALUES (21, 'Can add permission', 6, 'add_permission');
INSERT INTO `auth_permission` VALUES (22, 'Can change permission', 6, 'change_permission');
INSERT INTO `auth_permission` VALUES (23, 'Can delete permission', 6, 'delete_permission');
INSERT INTO `auth_permission` VALUES (24, 'Can view permission', 6, 'view_permission');
INSERT INTO `auth_permission` VALUES (25, 'Can add post', 7, 'add_post');
INSERT INTO `auth_permission` VALUES (26, 'Can change post', 7, 'change_post');
INSERT INTO `auth_permission` VALUES (27, 'Can delete post', 7, 'delete_post');
INSERT INTO `auth_permission` VALUES (28, 'Can view post', 7, 'view_post');
INSERT INTO `auth_permission` VALUES (29, 'Can add role', 8, 'add_role');
INSERT INTO `auth_permission` VALUES (30, 'Can change role', 8, 'change_role');
INSERT INTO `auth_permission` VALUES (31, 'Can delete role', 8, 'delete_role');
INSERT INTO `auth_permission` VALUES (32, 'Can view role', 8, 'view_role');
INSERT INTO `auth_permission` VALUES (33, 'Can add dept', 9, 'add_dept');
INSERT INTO `auth_permission` VALUES (34, 'Can change dept', 9, 'change_dept');
INSERT INTO `auth_permission` VALUES (35, 'Can delete dept', 9, 'delete_dept');
INSERT INTO `auth_permission` VALUES (36, 'Can view dept', 9, 'view_dept');
INSERT INTO `auth_permission` VALUES (37, 'Can add 用户', 10, 'add_user');
INSERT INTO `auth_permission` VALUES (38, 'Can change 用户', 10, 'change_user');
INSERT INTO `auth_permission` VALUES (39, 'Can delete 用户', 10, 'delete_user');
INSERT INTO `auth_permission` VALUES (40, 'Can view 用户', 10, 'view_user');
INSERT INTO `auth_permission` VALUES (41, 'Can add 章节管理', 11, 'add_chapter');
INSERT INTO `auth_permission` VALUES (42, 'Can change 章节管理', 11, 'change_chapter');
INSERT INTO `auth_permission` VALUES (43, 'Can delete 章节管理', 11, 'delete_chapter');
INSERT INTO `auth_permission` VALUES (44, 'Can view 章节管理', 11, 'view_chapter');
INSERT INTO `auth_permission` VALUES (45, 'Can add learner lesson', 12, 'add_learnerlesson');
INSERT INTO `auth_permission` VALUES (46, 'Can change learner lesson', 12, 'change_learnerlesson');
INSERT INTO `auth_permission` VALUES (47, 'Can delete learner lesson', 12, 'delete_learnerlesson');
INSERT INTO `auth_permission` VALUES (48, 'Can view learner lesson', 12, 'view_learnerlesson');
INSERT INTO `auth_permission` VALUES (49, 'Can add 课程管理', 13, 'add_lesson');
INSERT INTO `auth_permission` VALUES (50, 'Can change 课程管理', 13, 'change_lesson');
INSERT INTO `auth_permission` VALUES (51, 'Can delete 课程管理', 13, 'delete_lesson');
INSERT INTO `auth_permission` VALUES (52, 'Can view 课程管理', 13, 'view_lesson');
INSERT INTO `auth_permission` VALUES (53, 'Can add chapter lesson', 14, 'add_chapterlesson');
INSERT INTO `auth_permission` VALUES (54, 'Can change chapter lesson', 14, 'change_chapterlesson');
INSERT INTO `auth_permission` VALUES (55, 'Can delete chapter lesson', 14, 'delete_chapterlesson');
INSERT INTO `auth_permission` VALUES (56, 'Can view chapter lesson', 14, 'view_chapterlesson');
INSERT INTO `auth_permission` VALUES (57, 'Can add learner chapter', 15, 'add_learnerchapter');
INSERT INTO `auth_permission` VALUES (58, 'Can change learner chapter', 15, 'change_learnerchapter');
INSERT INTO `auth_permission` VALUES (59, 'Can delete learner chapter', 15, 'delete_learnerchapter');
INSERT INTO `auth_permission` VALUES (60, 'Can view learner chapter', 15, 'view_learnerchapter');
INSERT INTO `auth_permission` VALUES (61, 'Can add menu', 16, 'add_menu');
INSERT INTO `auth_permission` VALUES (62, 'Can change menu', 16, 'change_menu');
INSERT INTO `auth_permission` VALUES (63, 'Can delete menu', 16, 'delete_menu');
INSERT INTO `auth_permission` VALUES (64, 'Can view menu', 16, 'view_menu');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL,
  `object_repr` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `content_type_id` int NULL DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `django_admin_log_content_type_id_c4bce8eb_fk_django_co`(`content_type_id`) USING BTREE,
  INDEX `django_admin_log_user_id_c564eba6_fk_rbac_user_id`(`user_id`) USING BTREE,
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_rbac_user_id` FOREIGN KEY (`user_id`) REFERENCES `rbac_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 61 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES (1, '2021-08-28 10:28:20.030104', '1', 'Dept:信息学院 parentDept:None', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (2, '2021-08-28 10:28:49.053239', '2', 'Dept:研究生 parentDept:Dept:信息学院 parentDept:None', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (3, '2021-08-28 10:32:11.026355', '1', '高等数学1', 1, '[{\"added\": {}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (4, '2021-08-28 10:32:24.280229', '1', '数学', 2, '[{\"changed\": {\"fields\": [\"\\u8bfe\\u7a0b\\u540d\\u79f0\"]}}]', 13, 1);
INSERT INTO `django_admin_log` VALUES (5, '2021-08-28 10:36:08.515037', '1', '高等数学上', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (6, '2021-08-28 10:36:22.313536', '2', '高等数学下', 1, '[{\"added\": {}}]', 11, 1);
INSERT INTO `django_admin_log` VALUES (7, '2021-08-28 10:38:07.604196', '1', 'LearnerChapter object (1)', 1, '[{\"added\": {}}]', 15, 1);
INSERT INTO `django_admin_log` VALUES (8, '2021-08-28 10:40:22.617633', '1', 'LearnerLesson object (1)', 1, '[{\"added\": {}}]', 12, 1);
INSERT INTO `django_admin_log` VALUES (9, '2021-08-28 10:41:29.907889', '1', 'ChapterLesson object (1)', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (10, '2021-08-28 10:41:50.688374', '1', 'ChapterLesson object (1)', 2, '[]', 14, 1);
INSERT INTO `django_admin_log` VALUES (11, '2021-08-28 10:42:10.097568', '2', 'ChapterLesson object (2)', 1, '[{\"added\": {}}]', 14, 1);
INSERT INTO `django_admin_log` VALUES (12, '2021-08-28 10:43:52.899752', '1', '信息学院', 2, '[]', 9, 1);
INSERT INTO `django_admin_log` VALUES (13, '2021-08-28 10:44:02.119783', '3', '北京化工大学', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (14, '2021-08-28 10:44:11.746529', '2', '研究生', 3, '', 9, 1);
INSERT INTO `django_admin_log` VALUES (15, '2021-08-28 10:44:30.624101', '4', '计算机系', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (16, '2021-08-28 10:45:14.257559', '1', '本科生', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (17, '2021-08-28 10:45:18.407839', '2', '研究生', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (18, '2021-08-28 10:48:21.065063', '1', 'yangyu', 2, '[{\"changed\": {\"fields\": [\"Last login\", \"\\u6240\\u5c5e\\u90e8\\u95e8\", \"\\u5173\\u8054\\u89d2\\u8272\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (19, '2021-08-28 10:49:58.110236', '3', '管理员', 1, '[{\"added\": {}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (20, '2021-08-28 10:50:13.817982', '1', '增加课程', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (21, '2021-08-28 10:51:17.959017', '2', '删除课程', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (22, '2021-08-28 10:51:29.214613', '3', '管理员', 2, '[{\"changed\": {\"fields\": [\"\\u89d2\\u8272\\u6240\\u6709\\u6743\\u9650\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (23, '2021-08-28 10:52:20.898044', '1', 'yangyu', 2, '[{\"changed\": {\"fields\": [\"\\u5173\\u8054\\u89d2\\u8272\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (24, '2021-08-28 10:53:20.054623', '1', '学生', 1, '[{\"added\": {}}]', 7, 1);
INSERT INTO `django_admin_log` VALUES (25, '2021-08-28 10:53:47.228076', '1', 'yangyu', 2, '[{\"changed\": {\"fields\": [\"\\u7528\\u6237\\u59d3\\u540d\", \"\\u6240\\u5c5e\\u5c97\\u4f4d\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (26, '2021-08-30 08:06:02.464530', '1', '信息学院', 2, '[{\"changed\": {\"fields\": [\"\\u4e0a\\u7ea7\\u90e8\\u95e8\"]}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (27, '2021-08-30 10:33:54.091559', '2', '研究生', 2, '[{\"changed\": {\"fields\": [\"\\u89d2\\u8272\\u6240\\u6709\\u6743\\u9650\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (28, '2021-08-30 12:29:44.247573', '5', '化工学院', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (29, '2021-08-30 12:29:53.392290', '6', '材料学院', 1, '[{\"added\": {}}]', 9, 1);
INSERT INTO `django_admin_log` VALUES (30, '2021-09-02 10:23:21.210967', '1', 'Menu object (1)', 1, '[{\"added\": {}}]', 16, 1);
INSERT INTO `django_admin_log` VALUES (31, '2021-09-02 10:25:53.598554', '2', '删除课程', 2, '[{\"changed\": {\"fields\": [\"\\u83dc\\u5355\"]}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (32, '2021-09-02 10:26:00.153440', '1', '增加课程', 2, '[{\"changed\": {\"fields\": [\"\\u83dc\\u5355\"]}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (33, '2021-09-02 11:23:42.974107', '2', '系统管理', 1, '[{\"added\": {}}]', 16, 1);
INSERT INTO `django_admin_log` VALUES (34, '2021-09-02 11:24:17.915612', '3', '用户管理', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (35, '2021-09-02 11:24:24.792656', '3', '用户管理', 2, '[{\"changed\": {\"fields\": [\"\\u83dc\\u5355\"]}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (36, '2021-09-02 14:44:37.375814', '4', '用户管理', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (37, '2021-09-02 14:44:51.871050', '5', '权限管理', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (38, '2021-09-02 14:45:17.659027', '6', '部门管理', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (39, '2021-09-02 14:45:41.710305', '7', '岗位管理', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (40, '2021-09-02 14:46:06.459035', '3', '用户管理', 3, '', 6, 1);
INSERT INTO `django_admin_log` VALUES (41, '2021-09-02 14:52:06.124979', '3', '管理员', 2, '[{\"changed\": {\"fields\": [\"\\u89d2\\u8272\\u6240\\u6709\\u6743\\u9650\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (42, '2021-09-02 14:53:14.142211', '8', '角色管理', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (43, '2021-09-02 14:53:53.981855', '3', '管理员', 2, '[{\"changed\": {\"fields\": [\"\\u89d2\\u8272\\u6240\\u6709\\u6743\\u9650\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (44, '2021-09-02 14:55:18.205000', '2', '删除课程', 2, '[{\"changed\": {\"fields\": [\"\\u83dc\\u5355\"]}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (45, '2021-09-02 14:55:22.082878', '1', '增加课程', 2, '[{\"changed\": {\"fields\": [\"\\u83dc\\u5355\"]}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (46, '2021-09-02 22:25:45.283124', '3', '训练管理', 1, '[{\"added\": {}}]', 16, 1);
INSERT INTO `django_admin_log` VALUES (47, '2021-09-02 22:25:58.427417', '4', '数据统计', 1, '[{\"added\": {}}]', 16, 1);
INSERT INTO `django_admin_log` VALUES (48, '2021-09-02 22:30:36.192555', '9', '课程列表', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (49, '2021-09-02 22:31:10.186769', '10', '学习课程', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (50, '2021-09-02 22:31:12.152630', '10', '学习课程', 2, '[]', 6, 1);
INSERT INTO `django_admin_log` VALUES (51, '2021-09-02 22:33:32.620391', '11', '章节管理', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (52, '2021-09-02 22:34:26.799160', '11', '章节列表', 2, '[{\"changed\": {\"fields\": [\"\\u6743\\u9650\\u540d\\u79f0\"]}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (53, '2021-09-02 22:35:41.406074', '12', '训练列表', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (54, '2021-09-02 22:36:31.439828', '13', '参加训练', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (55, '2021-09-02 22:37:47.862801', '14', '成绩分析', 1, '[{\"added\": {}}]', 6, 1);
INSERT INTO `django_admin_log` VALUES (56, '2021-09-02 22:38:05.410977', '2', '研究生', 3, '', 8, 1);
INSERT INTO `django_admin_log` VALUES (57, '2021-09-02 22:38:05.423833', '1', '本科生', 3, '', 8, 1);
INSERT INTO `django_admin_log` VALUES (58, '2021-09-02 22:38:44.656599', '3', '管理员', 2, '[{\"changed\": {\"fields\": [\"\\u89d2\\u8272\\u6240\\u6709\\u6743\\u9650\"]}}]', 8, 1);
INSERT INTO `django_admin_log` VALUES (59, '2021-09-02 22:39:11.227339', '3', 'sm', 2, '[{\"changed\": {\"fields\": [\"\\u5173\\u8054\\u89d2\\u8272\"]}}]', 10, 1);
INSERT INTO `django_admin_log` VALUES (60, '2021-09-03 10:54:53.396038', '4', '用户管理', 2, '[{\"changed\": {\"fields\": [\"\\u63a5\\u53e3URL\", \"\\u524d\\u7aef\\u8def\\u7531path\"]}}]', 6, 1);

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `model` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `django_content_type_app_label_model_76bd3d3b_uniq`(`app_label`, `model`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES (1, 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES (3, 'auth', 'group');
INSERT INTO `django_content_type` VALUES (2, 'auth', 'permission');
INSERT INTO `django_content_type` VALUES (4, 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES (11, 'lesson', 'chapter');
INSERT INTO `django_content_type` VALUES (14, 'lesson', 'chapterlesson');
INSERT INTO `django_content_type` VALUES (15, 'lesson', 'learnerchapter');
INSERT INTO `django_content_type` VALUES (12, 'lesson', 'learnerlesson');
INSERT INTO `django_content_type` VALUES (13, 'lesson', 'lesson');
INSERT INTO `django_content_type` VALUES (9, 'rbac', 'dept');
INSERT INTO `django_content_type` VALUES (16, 'rbac', 'menu');
INSERT INTO `django_content_type` VALUES (6, 'rbac', 'permission');
INSERT INTO `django_content_type` VALUES (7, 'rbac', 'post');
INSERT INTO `django_content_type` VALUES (8, 'rbac', 'role');
INSERT INTO `django_content_type` VALUES (10, 'rbac', 'user');
INSERT INTO `django_content_type` VALUES (5, 'sessions', 'session');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES (1, 'rbac', '0001_initial', '2021-08-28 09:16:40.218192');
INSERT INTO `django_migrations` VALUES (2, 'contenttypes', '0001_initial', '2021-08-28 09:16:40.344498');
INSERT INTO `django_migrations` VALUES (3, 'admin', '0001_initial', '2021-08-28 09:16:40.599413');
INSERT INTO `django_migrations` VALUES (4, 'admin', '0002_logentry_remove_auto_add', '2021-08-28 09:16:40.623609');
INSERT INTO `django_migrations` VALUES (5, 'admin', '0003_logentry_add_action_flag_choices', '2021-08-28 09:16:40.650785');
INSERT INTO `django_migrations` VALUES (6, 'contenttypes', '0002_remove_content_type_name', '2021-08-28 09:16:40.813447');
INSERT INTO `django_migrations` VALUES (7, 'auth', '0001_initial', '2021-08-28 09:16:41.295899');
INSERT INTO `django_migrations` VALUES (8, 'auth', '0002_alter_permission_name_max_length', '2021-08-28 09:16:41.435381');
INSERT INTO `django_migrations` VALUES (9, 'auth', '0003_alter_user_email_max_length', '2021-08-28 09:16:41.470716');
INSERT INTO `django_migrations` VALUES (10, 'auth', '0004_alter_user_username_opts', '2021-08-28 09:16:41.495774');
INSERT INTO `django_migrations` VALUES (11, 'auth', '0005_alter_user_last_login_null', '2021-08-28 09:16:41.520265');
INSERT INTO `django_migrations` VALUES (12, 'auth', '0006_require_contenttypes_0002', '2021-08-28 09:16:41.538621');
INSERT INTO `django_migrations` VALUES (13, 'auth', '0007_alter_validators_add_error_messages', '2021-08-28 09:16:41.566393');
INSERT INTO `django_migrations` VALUES (14, 'auth', '0008_alter_user_username_max_length', '2021-08-28 09:16:41.592029');
INSERT INTO `django_migrations` VALUES (15, 'auth', '0009_alter_user_last_name_max_length', '2021-08-28 09:16:41.621626');
INSERT INTO `django_migrations` VALUES (16, 'auth', '0010_alter_group_name_max_length', '2021-08-28 09:16:41.663836');
INSERT INTO `django_migrations` VALUES (17, 'auth', '0011_update_proxy_permissions', '2021-08-28 09:16:41.719924');
INSERT INTO `django_migrations` VALUES (18, 'auth', '0012_alter_user_first_name_max_length', '2021-08-28 09:16:41.743189');
INSERT INTO `django_migrations` VALUES (19, 'sessions', '0001_initial', '2021-08-28 09:16:41.829120');
INSERT INTO `django_migrations` VALUES (20, 'rbac', '0002_user_email', '2021-08-28 09:20:10.896642');
INSERT INTO `django_migrations` VALUES (21, 'lesson', '0001_initial', '2021-08-28 10:06:44.053917');
INSERT INTO `django_migrations` VALUES (22, 'lesson', '0002_alter_lesson_learners', '2021-08-28 10:13:13.038490');
INSERT INTO `django_migrations` VALUES (23, 'lesson', '0003_auto_20210828_1823', '2021-08-28 10:23:35.100084');
INSERT INTO `django_migrations` VALUES (24, 'lesson', '0004_auto_20210828_1839', '2021-08-28 10:40:02.931067');
INSERT INTO `django_migrations` VALUES (25, 'rbac', '0003_auto_20210828_1839', '2021-08-28 10:40:03.081240');
INSERT INTO `django_migrations` VALUES (26, 'lesson', '0005_alter_chapterlesson_prev', '2021-08-28 10:41:43.274579');
INSERT INTO `django_migrations` VALUES (27, 'rbac', '0004_alter_post_options', '2021-08-28 10:53:05.073234');
INSERT INTO `django_migrations` VALUES (28, 'rbac', '0005_rename_parent_dept_parentdept', '2021-08-30 06:43:32.026891');
INSERT INTO `django_migrations` VALUES (29, 'rbac', '0006_auto_20210902_1019', '2021-09-02 10:19:55.506273');
INSERT INTO `django_migrations` VALUES (30, 'rbac', '0007_auto_20210902_1123', '2021-09-02 11:23:37.241533');
INSERT INTO `django_migrations` VALUES (31, 'rbac', '0008_auto_20210903_1039', '2021-09-03 10:40:06.957628');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session`  (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`) USING BTREE,
  INDEX `django_session_expire_date_a5c62663`(`expire_date`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('pyuvqfhg8hvb6y9zvu9tctiy8e4g53di', '.eJxVjDsOwyAQBe9CHSEWsYBTps8Z0C6f4CTCkrErK3ePLblI2jczbxOB1qWGtec5jElcBYjL78YUX7kdID2pPSYZp7bMI8tDkSft8j6l_L6d7t9BpV73mowxoMtAyDCwJXDkTVGgOGIElQCtY0WuFLYFo0K9W8VnjeSIvRKfL9wNN-k:1mLcJV:w3nSc0olc_4DM53C_kdfamzqOrZ693JCxZKg5Ke4ytc', '2021-09-16 10:18:49.301008');
INSERT INTO `django_session` VALUES ('vfeg1zrz0zeqq2jbu1kucpw8e5kxb0gz', '.eJxVjDsOwyAQBe9CHSEWsYBTps8Z0C6f4CTCkrErK3ePLblI2jczbxOB1qWGtec5jElcBYjL78YUX7kdID2pPSYZp7bMI8tDkSft8j6l_L6d7t9BpV73mowxoMtAyDCwJXDkTVGgOGIElQCtY0WuFLYFo0K9W8VnjeSIvRKfL9wNN-k:1mLhNV:m59utwAvwm51L19RtUHlY4PnFH3GyoU1Frcc2Of2-LA', '2021-09-16 15:43:17.437330');

-- ----------------------------
-- Table structure for lesson_chapter
-- ----------------------------
DROP TABLE IF EXISTS `lesson_chapter`;
CREATE TABLE `lesson_chapter`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `ChapterID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `ChapterName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `ChapterURL` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `ChapterID`(`ChapterID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lesson_chapter
-- ----------------------------
INSERT INTO `lesson_chapter` VALUES (1, 'GDSX1', '高等数学上', NULL);
INSERT INTO `lesson_chapter` VALUES (2, 'GDSX2', '高等数学下', NULL);

-- ----------------------------
-- Table structure for lesson_chapterlesson
-- ----------------------------
DROP TABLE IF EXISTS `lesson_chapterlesson`;
CREATE TABLE `lesson_chapterlesson`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `chapter_id` bigint NOT NULL,
  `lesson_id` bigint NOT NULL,
  `prev_id` bigint NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `lesson_chapterlesson_chapter_id_cf576912_fk_lesson_chapter_id`(`chapter_id`) USING BTREE,
  INDEX `lesson_chapterlesson_lesson_id_9e02f112_fk_lesson_lesson_id`(`lesson_id`) USING BTREE,
  INDEX `lesson_chapterlesson_prev_id_057afd5c_fk_lesson_chapter_id`(`prev_id`) USING BTREE,
  CONSTRAINT `lesson_chapterlesson_chapter_id_cf576912_fk_lesson_chapter_id` FOREIGN KEY (`chapter_id`) REFERENCES `lesson_chapter` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `lesson_chapterlesson_lesson_id_9e02f112_fk_lesson_lesson_id` FOREIGN KEY (`lesson_id`) REFERENCES `lesson_lesson` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `lesson_chapterlesson_prev_id_057afd5c_fk_lesson_chapter_id` FOREIGN KEY (`prev_id`) REFERENCES `lesson_chapter` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lesson_chapterlesson
-- ----------------------------
INSERT INTO `lesson_chapterlesson` VALUES (1, 1, 1, NULL);
INSERT INTO `lesson_chapterlesson` VALUES (2, 2, 1, 1);

-- ----------------------------
-- Table structure for lesson_learnerchapter
-- ----------------------------
DROP TABLE IF EXISTS `lesson_learnerchapter`;
CREATE TABLE `lesson_learnerchapter`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NULL DEFAULT NULL,
  `chapter_id` bigint NOT NULL,
  `learner_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `lesson_learnerchapter_chapter_id_191c5fb8_fk_lesson_chapter_id`(`chapter_id`) USING BTREE,
  INDEX `lesson_learnerchapter_learner_id_474fdb25_fk_rbac_user_id`(`learner_id`) USING BTREE,
  CONSTRAINT `lesson_learnerchapter_chapter_id_191c5fb8_fk_lesson_chapter_id` FOREIGN KEY (`chapter_id`) REFERENCES `lesson_chapter` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `lesson_learnerchapter_learner_id_474fdb25_fk_rbac_user_id` FOREIGN KEY (`learner_id`) REFERENCES `rbac_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lesson_learnerchapter
-- ----------------------------
INSERT INTO `lesson_learnerchapter` VALUES (1, 0, 1, 1);

-- ----------------------------
-- Table structure for lesson_learnerlesson
-- ----------------------------
DROP TABLE IF EXISTS `lesson_learnerlesson`;
CREATE TABLE `lesson_learnerlesson`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `status` tinyint(1) NULL DEFAULT NULL,
  `learner_id` bigint NOT NULL,
  `lesson_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `lesson_learnerlesson_lesson_id_f14224a0_fk_lesson_lesson_id`(`lesson_id`) USING BTREE,
  INDEX `lesson_learnerlesson_learner_id_ca132eac_fk_rbac_user_id`(`learner_id`) USING BTREE,
  CONSTRAINT `lesson_learnerlesson_learner_id_ca132eac_fk_rbac_user_id` FOREIGN KEY (`learner_id`) REFERENCES `rbac_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `lesson_learnerlesson_lesson_id_f14224a0_fk_lesson_lesson_id` FOREIGN KEY (`lesson_id`) REFERENCES `lesson_lesson` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lesson_learnerlesson
-- ----------------------------
INSERT INTO `lesson_learnerlesson` VALUES (1, 0, 1, 1);

-- ----------------------------
-- Table structure for lesson_lesson
-- ----------------------------
DROP TABLE IF EXISTS `lesson_lesson`;
CREATE TABLE `lesson_lesson`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `LessonID` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `LessonName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `detail` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `LessonID`(`LessonID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lesson_lesson
-- ----------------------------
INSERT INTO `lesson_lesson` VALUES (1, 'MATH', '数学', NULL);

-- ----------------------------
-- Table structure for rbac_dept
-- ----------------------------
DROP TABLE IF EXISTS `rbac_dept`;
CREATE TABLE `rbac_dept`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `parentDept_id` bigint NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `rbac_dept_parentDept_id_dd031783_fk_rbac_dept_id`(`parentDept_id`) USING BTREE,
  CONSTRAINT `rbac_dept_parentDept_id_dd031783_fk_rbac_dept_id` FOREIGN KEY (`parentDept_id`) REFERENCES `rbac_dept` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rbac_dept
-- ----------------------------
INSERT INTO `rbac_dept` VALUES (1, '信息学院', 3);
INSERT INTO `rbac_dept` VALUES (3, '北京化工大学', NULL);
INSERT INTO `rbac_dept` VALUES (4, '计算机系', 1);
INSERT INTO `rbac_dept` VALUES (5, '化工学院', 3);
INSERT INTO `rbac_dept` VALUES (6, '材料学院', 3);

-- ----------------------------
-- Table structure for rbac_menu
-- ----------------------------
DROP TABLE IF EXISTS `rbac_menu`;
CREATE TABLE `rbac_menu`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `icon` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `title`(`title`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rbac_menu
-- ----------------------------
INSERT INTO `rbac_menu` VALUES (1, '课程管理', NULL);
INSERT INTO `rbac_menu` VALUES (2, '系统管理', NULL);
INSERT INTO `rbac_menu` VALUES (3, '训练管理', NULL);
INSERT INTO `rbac_menu` VALUES (4, '数据统计', NULL);

-- ----------------------------
-- Table structure for rbac_permission
-- ----------------------------
DROP TABLE IF EXISTS `rbac_permission`;
CREATE TABLE `rbac_permission`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `url` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `menu_id` bigint NULL DEFAULT NULL,
  `path` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `rbac_permission_menu_id_3dcc68be_fk_rbac_menu_id`(`menu_id`) USING BTREE,
  CONSTRAINT `rbac_permission_menu_id_3dcc68be_fk_rbac_menu_id` FOREIGN KEY (`menu_id`) REFERENCES `rbac_menu` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 15 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rbac_permission
-- ----------------------------
INSERT INTO `rbac_permission` VALUES (1, '增加课程', '/lesson/add', NULL, NULL);
INSERT INTO `rbac_permission` VALUES (2, '删除课程', '/lesson/delete', NULL, NULL);
INSERT INTO `rbac_permission` VALUES (4, '用户管理', '/user/list/', 2, '/user/');
INSERT INTO `rbac_permission` VALUES (5, '权限管理', '/permission/list', 2, NULL);
INSERT INTO `rbac_permission` VALUES (6, '部门管理', '/dept/list', 2, NULL);
INSERT INTO `rbac_permission` VALUES (7, '岗位管理', '/post/list', 2, NULL);
INSERT INTO `rbac_permission` VALUES (8, '角色管理', '/role/list', 2, NULL);
INSERT INTO `rbac_permission` VALUES (9, '课程列表', '/lesson/list', 1, NULL);
INSERT INTO `rbac_permission` VALUES (10, '学习课程', '/lesson/', 1, NULL);
INSERT INTO `rbac_permission` VALUES (11, '章节列表', '/chapter', 1, NULL);
INSERT INTO `rbac_permission` VALUES (12, '训练列表', '/train', 3, NULL);
INSERT INTO `rbac_permission` VALUES (13, '参加训练', '/train/', 3, NULL);
INSERT INTO `rbac_permission` VALUES (14, '成绩分析', '/socre', 4, NULL);

-- ----------------------------
-- Table structure for rbac_post
-- ----------------------------
DROP TABLE IF EXISTS `rbac_post`;
CREATE TABLE `rbac_post`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rbac_post
-- ----------------------------
INSERT INTO `rbac_post` VALUES (1, '学生');

-- ----------------------------
-- Table structure for rbac_role
-- ----------------------------
DROP TABLE IF EXISTS `rbac_role`;
CREATE TABLE `rbac_role`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `title` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rbac_role
-- ----------------------------
INSERT INTO `rbac_role` VALUES (3, '管理员');

-- ----------------------------
-- Table structure for rbac_role_permissions
-- ----------------------------
DROP TABLE IF EXISTS `rbac_role_permissions`;
CREATE TABLE `rbac_role_permissions`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `role_id` bigint NOT NULL,
  `permission_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `rbac_role_permissions_role_id_permission_id_d01303da_uniq`(`role_id`, `permission_id`) USING BTREE,
  INDEX `rbac_role_permission_permission_id_f5e1e866_fk_rbac_perm`(`permission_id`) USING BTREE,
  CONSTRAINT `rbac_role_permission_permission_id_f5e1e866_fk_rbac_perm` FOREIGN KEY (`permission_id`) REFERENCES `rbac_permission` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `rbac_role_permissions_role_id_d10416cb_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 17 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rbac_role_permissions
-- ----------------------------
INSERT INTO `rbac_role_permissions` VALUES (9, 3, 1);
INSERT INTO `rbac_role_permissions` VALUES (10, 3, 2);
INSERT INTO `rbac_role_permissions` VALUES (4, 3, 4);
INSERT INTO `rbac_role_permissions` VALUES (5, 3, 5);
INSERT INTO `rbac_role_permissions` VALUES (6, 3, 6);
INSERT INTO `rbac_role_permissions` VALUES (7, 3, 7);
INSERT INTO `rbac_role_permissions` VALUES (8, 3, 8);
INSERT INTO `rbac_role_permissions` VALUES (11, 3, 9);
INSERT INTO `rbac_role_permissions` VALUES (12, 3, 10);
INSERT INTO `rbac_role_permissions` VALUES (13, 3, 11);
INSERT INTO `rbac_role_permissions` VALUES (14, 3, 12);
INSERT INTO `rbac_role_permissions` VALUES (15, 3, 13);
INSERT INTO `rbac_role_permissions` VALUES (16, 3, 14);

-- ----------------------------
-- Table structure for rbac_user
-- ----------------------------
DROP TABLE IF EXISTS `rbac_user`;
CREATE TABLE `rbac_user`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `last_login` datetime(6) NULL DEFAULT NULL,
  `username` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `dept_id` bigint NULL DEFAULT NULL,
  `post_id` bigint NULL DEFAULT NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `username`(`username`) USING BTREE,
  INDEX `rbac_user_dept_id_1b5bdb0d_fk_rbac_dept_id`(`dept_id`) USING BTREE,
  INDEX `rbac_user_post_id_b7d7c986_fk_rbac_post_id`(`post_id`) USING BTREE,
  CONSTRAINT `rbac_user_dept_id_1b5bdb0d_fk_rbac_dept_id` FOREIGN KEY (`dept_id`) REFERENCES `rbac_dept` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `rbac_user_post_id_b7d7c986_fk_rbac_post_id` FOREIGN KEY (`post_id`) REFERENCES `rbac_post` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rbac_user
-- ----------------------------
INSERT INTO `rbac_user` VALUES (1, 'pbkdf2_sha256$260000$oZcBBsGPnxQb3PXUn9pkUB$NdRNKrIR7rKiT8oglIQxkDBJqOi0RJAizoFq39MNsN4=', '2021-09-02 15:43:17.422548', 'yangyu', '杨宇', 0, 1, '2021-08-28 09:18:14.750319', 4, 1, NULL);
INSERT INTO `rbac_user` VALUES (2, 'pbkdf2_sha256$260000$CGGrSyj1L4C8ow4hoM2ZI7$1a72Bc98irBgsmnuR6SvvUPBzXPbUp3GoxQ2u90zSbw=', NULL, '2021200726', NULL, 1, 1, '2021-08-30 11:56:06.967128', NULL, NULL, NULL);
INSERT INTO `rbac_user` VALUES (3, 'pbkdf2_sha256$260000$raoKGBMkuJuRT7iOXGuG0k$92VVYU2XtyPa35o+t5MpugeyynrdoSISotM8/VPFt9c=', NULL, 'sm', NULL, 1, 1, '2021-09-02 15:44:13.758980', NULL, NULL, NULL);
INSERT INTO `rbac_user` VALUES (4, '123456', NULL, 'lrq', NULL, 1, 0, '2021-09-03 16:18:08.068479', 4, 1, NULL);
INSERT INTO `rbac_user` VALUES (5, '123456', NULL, 'lugang', NULL, 1, 0, '2021-09-03 16:25:01.402801', 4, 1, NULL);
INSERT INTO `rbac_user` VALUES (6, '123456', NULL, 'guweiwei', NULL, 1, 0, '2021-09-03 16:25:01.581853', 4, 1, NULL);
INSERT INTO `rbac_user` VALUES (7, '1234567', NULL, 'yangao', NULL, 0, 0, '2021-09-03 20:23:15.638407', 4, 1, NULL);
INSERT INTO `rbac_user` VALUES (8, '1234567', NULL, 'gaotianli', NULL, 0, 0, '2021-09-03 20:23:15.692692', 4, 1, NULL);
INSERT INTO `rbac_user` VALUES (9, '123456', NULL, 'jingjing', NULL, 0, 0, '2021-09-03 21:05:54.506800', 4, 1, NULL);
INSERT INTO `rbac_user` VALUES (10, '123456', NULL, 'cty', NULL, 0, 0, '2021-09-03 21:05:54.558809', 4, 1, NULL);

-- ----------------------------
-- Table structure for rbac_user_roles
-- ----------------------------
DROP TABLE IF EXISTS `rbac_user_roles`;
CREATE TABLE `rbac_user_roles`  (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `role_id` bigint NOT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `rbac_user_roles_user_id_role_id_60665088_uniq`(`user_id`, `role_id`) USING BTREE,
  INDEX `rbac_user_roles_role_id_363ee4fe_fk_rbac_role_id`(`role_id`) USING BTREE,
  CONSTRAINT `rbac_user_roles_role_id_363ee4fe_fk_rbac_role_id` FOREIGN KEY (`role_id`) REFERENCES `rbac_role` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `rbac_user_roles_user_id_01d9ab9e_fk_rbac_user_id` FOREIGN KEY (`user_id`) REFERENCES `rbac_user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 11 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of rbac_user_roles
-- ----------------------------
INSERT INTO `rbac_user_roles` VALUES (2, 1, 3);
INSERT INTO `rbac_user_roles` VALUES (3, 3, 3);
INSERT INTO `rbac_user_roles` VALUES (4, 4, 3);
INSERT INTO `rbac_user_roles` VALUES (5, 5, 3);
INSERT INTO `rbac_user_roles` VALUES (6, 6, 3);
INSERT INTO `rbac_user_roles` VALUES (7, 7, 3);
INSERT INTO `rbac_user_roles` VALUES (8, 8, 3);
INSERT INTO `rbac_user_roles` VALUES (9, 9, 3);
INSERT INTO `rbac_user_roles` VALUES (10, 10, 3);

SET FOREIGN_KEY_CHECKS = 1;
