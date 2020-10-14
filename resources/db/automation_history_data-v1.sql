-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 14, 2020 at 03:01 AM
-- Server version: 8.0.21
-- PHP Version: 7.1.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `automation_history`
--

-- --------------------------------------------------------

--
-- Table structure for table `browser`
--

CREATE TABLE `browser` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `alias` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `browser`
--

INSERT INTO `browser` (`id`, `name`, `alias`, `version`, `create_time`, `update_time`) VALUES
(1, 'Chrome', 'chrome', '75.0.3770.142', '2019-07-31 02:46:21', '2019-07-31 02:46:21'),
(2, 'Firefox', 'firefox', '67.0.4', '2019-07-31 02:48:37', '2019-07-31 02:48:37'),
(3, 'Safari', 'Safari', '12.1.2', '2019-07-31 02:49:54', '2019-07-31 02:49:54'),
(4, 'IE', 'internet explorer', '11', '2019-07-31 02:53:20', '2019-07-31 02:53:20'),
(5, 'Edge', 'MicrosoftEdge', '42.17134.1.0', '2019-07-31 02:54:49', '2019-07-31 02:54:49'),
(6, 'MobileBrowser', 'chrome', '75.0.3770.142', '2019-07-31 02:56:31', '2019-07-31 02:56:31'),
(7, 'Chrome', 'chrome', '76.0.3809.100', '2019-10-27 04:06:59', '2019-10-27 04:06:59'),
(8, 'Chrome', 'chrome', '80.0.3987.132', '2020-03-10 06:23:05', '2020-03-10 06:23:05'),
(9, 'Chrome', 'chrome', 'unknown', '2020-03-21 02:05:19', '2020-03-21 02:05:19'),
(10, 'Chrome', 'chrome', '80.0.3987.149', '2020-03-21 02:09:52', '2020-03-21 02:09:52');

-- --------------------------------------------------------

--
-- Table structure for table `case_suite`
--

CREATE TABLE `case_suite` (
  `id` int NOT NULL,
  `test_suite_id` int NOT NULL,
  `test_case_id` int NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `case_suite`
--

INSERT INTO `case_suite` (`id`, `test_suite_id`, `test_case_id`, `create_time`, `update_time`) VALUES
(1, 1, 1, '2019-10-27 03:50:03', '2019-10-27 03:50:03'),
(2, 1, 2, '2019-10-27 03:50:07', '2019-10-27 03:50:07'),
(3, 1, 3, '2019-10-27 03:50:11', '2019-10-27 03:50:11'),
(4, 1, 4, '2019-10-27 03:50:16', '2019-10-27 03:50:16'),
(5, 1, 5, '2019-10-27 03:50:20', '2019-10-27 03:50:20'),
(6, 2, 6, '2019-10-27 04:07:10', '2019-10-27 04:07:10'),
(7, 2, 7, '2019-10-27 04:07:15', '2019-10-27 04:07:15'),
(8, 2, 8, '2019-10-27 04:07:19', '2019-10-27 04:07:19'),
(9, 2, 9, '2019-10-27 04:07:23', '2019-10-27 04:07:23'),
(10, 3, 10, '2019-10-27 04:10:37', '2019-10-27 04:10:37'),
(11, 8, 6, '2020-03-21 02:10:02', '2020-03-21 02:10:02'),
(12, 8, 9, '2020-03-21 02:10:08', '2020-03-21 02:10:08'),
(13, 8, 7, '2020-03-21 02:10:14', '2020-03-21 02:10:14');

-- --------------------------------------------------------

--
-- Table structure for table `device`
--

CREATE TABLE `device` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `device`
--

INSERT INTO `device` (`id`, `name`, `create_time`, `update_time`) VALUES
(1, 'Simulator', '2019-07-31 06:26:04', '2019-07-31 06:26:04'),
(2, 'Emulator', '2019-07-31 06:26:24', '2019-07-31 06:26:24'),
(3, 'MiPlus', '2019-07-31 06:26:43', '2019-07-31 06:26:43'),
(4, 'STF', '2019-07-31 06:26:49', '2019-07-31 06:26:49');

-- --------------------------------------------------------

--
-- Table structure for table `driver`
--

CREATE TABLE `driver` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `comment` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT;

--
-- Dumping data for table `driver`
--

INSERT INTO `driver` (`id`, `name`, `version`, `create_time`, `update_time`, `comment`) VALUES
(1, 'chromedriver', '74.0.3729.6', '2019-07-31 03:07:15', '2019-07-31 03:07:15', 'test on macos, chrome 74 and 75.0.3770.142'),
(2, 'geckodriver', '0.24.0', '2019-07-31 03:08:09', '2019-07-31 03:08:09', 'test on macos, firefox 67.0'),
(3, 'safaridriver', '12607.3.10', '2019-07-31 03:08:38', '2019-07-31 03:08:38', 'test on macos, safari 12.1.2'),
(4, 'IEDriver', '3.9.0.0', '2019-07-31 03:09:00', '2019-07-31 03:09:00', 'test on win10, ie 11.706.17134.0'),
(5, 'MicrosoftWebDriver\r\n', '17.17134', '2019-07-31 03:09:23', '2019-07-31 03:09:23', 'test on win10, Edge 17134'),
(6, 'appium', '1.11.1', '2019-07-31 03:11:13', '2019-07-31 03:11:13', 'test on macos 10.12.6, android 4.4.4 & 5.0.2 & 8.1.0, ios 11.2'),
(7, 'appium', '1.13.0', '2019-07-31 03:34:04', '2019-07-31 03:34:04', 'test on macos 10.14.6, android 8.1.0, ios 12.2 & 12.4');

-- --------------------------------------------------------

--
-- Table structure for table `mobile_os`
--

CREATE TABLE `mobile_os` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `mobile_os`
--

INSERT INTO `mobile_os` (`id`, `name`, `version`, `create_time`, `update_time`) VALUES
(1, 'iOS', '12.4', '2019-07-31 03:21:50', '2019-07-31 03:21:50'),
(2, 'Android', '8.1.0', '2019-07-31 03:22:49', '2019-07-31 03:22:49'),
(3, 'iOS', 'unknown', '2020-03-21 02:02:59', '2020-03-21 02:02:59');

-- --------------------------------------------------------

--
-- Table structure for table `platform_os`
--

CREATE TABLE `platform_os` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `version` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `platform_os`
--

INSERT INTO `platform_os` (`id`, `name`, `version`, `create_time`, `update_time`) VALUES
(1, 'Windows', 'Windows-10-10.0.17134-SP0', '2019-07-31 06:24:15', '2019-07-31 06:24:15'),
(2, 'Macos', 'Darwin-16.7.0-x86_64-i386-64bit', '2019-07-31 06:24:38', '2019-07-31 06:24:38'),
(3, 'Macos', 'Darwin-18.7.0-x86_64-i386-64bit', '2019-10-27 03:49:54', '2019-10-27 03:49:54'),
(4, 'Macos', 'Darwin-18.6.0-x86_64-i386-64bit', '2020-03-10 06:23:06', '2020-03-10 06:23:06');

-- --------------------------------------------------------

--
-- Table structure for table `project`
--

CREATE TABLE `project` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `project`
--

INSERT INTO `project` (`id`, `name`, `create_time`, `update_time`) VALUES
(1, 'rest_api', '2019-10-27 03:49:55', '2019-10-27 03:49:55'),
(2, 'byblog', '2019-10-27 04:07:03', '2019-10-27 04:07:03'),
(3, 'mobile_web', '2019-10-27 04:10:29', '2019-10-27 04:10:29');

-- --------------------------------------------------------

--
-- Table structure for table `test_case`
--

CREATE TABLE `test_case` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `test_function_id` int NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `test_case`
--

INSERT INTO `test_case` (`id`, `name`, `test_function_id`, `create_time`, `update_time`) VALUES
(1, 'RA-1: post comment amount 0', 1, '2019-10-27 03:50:02', '2019-10-27 03:50:02'),
(2, 'RA-2: post comment amount 1', 2, '2019-10-27 03:50:06', '2019-10-27 03:50:06'),
(3, 'RA-3: post comment amount 2', 3, '2019-10-27 03:50:10', '2019-10-27 03:50:10'),
(4, 'RA-4: posts amount', 4, '2019-10-27 03:50:15', '2019-10-27 03:50:15'),
(5, 'RA-5: create new post and check new amount', 5, '2019-10-27 03:50:19', '2019-10-27 03:50:19'),
(6, 'ByBlog-3: only user who have logged in can see the posts view dropdown in post list page', 6, '2019-10-27 04:07:09', '2019-10-27 04:07:09'),
(7, 'ByBlog-2: user is able to view posts when jump page', 7, '2019-10-27 04:07:14', '2019-10-27 04:07:14'),
(8, 'ByBlog-4: details page url contains post id', 8, '2019-10-27 04:07:18', '2019-10-27 04:07:18'),
(9, 'ByBlog-1: user is able to search posts and view the search result', 9, '2019-10-27 04:07:21', '2019-10-27 04:07:21'),
(10, 'MWeb-1: user is able to search posts and view the search result', 10, '2019-10-27 04:10:36', '2019-10-27 04:10:36');

-- --------------------------------------------------------

--
-- Table structure for table `test_case_result`
--

CREATE TABLE `test_case_result` (
  `id` int NOT NULL,
  `test_case_id` int NOT NULL,
  `test_round_id` int NOT NULL,
  `error_message` varchar(3000) DEFAULT NULL,
  `screenshot` varchar(500) DEFAULT NULL,
  `video` varchar(500) DEFAULT NULL,
  `result` varchar(100) NOT NULL,
  `data_driven` varchar(1000) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `test_case_result`
--

INSERT INTO `test_case_result` (`id`, `test_case_id`, `test_round_id`, `error_message`, `screenshot`, `video`, `result`, `data_driven`, `create_time`, `update_time`) VALUES
(1, 1, 1, NULL, NULL, NULL, 'pass', '1-a-500', '2019-10-27 03:51:59', '2019-10-27 03:51:59'),
(2, 1, 1, NULL, NULL, NULL, 'pass', '2-b-500', '2019-10-27 03:52:01', '2019-10-27 03:52:01'),
(3, 1, 1, NULL, NULL, NULL, 'pass', '4-d-500', '2019-10-27 03:52:02', '2019-10-27 03:52:02'),
(4, 2, 1, NULL, NULL, NULL, 'pass', '3-c-500', '2019-10-27 03:52:03', '2019-10-27 03:52:03'),
(5, 2, 1, NULL, NULL, NULL, 'pass', '7-b-500', '2019-10-27 03:52:04', '2019-10-27 03:52:04'),
(6, 3, 1, NULL, NULL, NULL, 'pass', '6', '2019-10-27 03:52:05', '2019-10-27 03:52:05'),
(7, 3, 1, NULL, NULL, NULL, 'pass', '99', '2019-10-27 03:52:06', '2019-10-27 03:52:06'),
(8, 1, 1, 'projects/rest_api/tests/test_post_comment.py:20: in test_post_comment_amount_0\n    assert comment_amount == expect_result, \"wrong comment amount of post 1\"\nE   AssertionError: wrong comment amount of post 1\nE   assert 500 == 501\nE     -500\nE     +501', NULL, NULL, 'fail', '3-c-501', '2019-10-27 03:52:07', '2019-10-27 03:52:07'),
(9, 4, 1, NULL, NULL, NULL, 'pass', NULL, '2019-10-27 03:52:08', '2019-10-27 03:52:08'),
(10, 5, 1, 'projects/rest_api/tests/test_posts.py:31: in test_create_new_post\n    assert all_posts_after == create_new_post_result[\"id\"], message_when_error\nE   AssertionError: amount is not correct after create new post, expect: 101, before create: 100\nE   assert 100 == 101\nE     -100\nE     +101', NULL, NULL, 'fail', NULL, '2019-10-27 03:52:09', '2019-10-27 03:52:09'),
(11, 6, 2, NULL, NULL, NULL, 'pass', NULL, '2019-10-27 04:07:31', '2019-10-27 04:07:31'),
(12, 7, 2, NULL, NULL, NULL, 'pass', NULL, '2019-10-27 04:07:32', '2019-10-27 04:07:32'),
(13, 8, 2, NULL, NULL, NULL, 'pass', NULL, '2019-10-27 04:07:33', '2019-10-27 04:07:33'),
(14, 9, 2, 'projects/byblog/tests/test_view_posts.py:12: in test_view_posts_in_search_result\n    self.main_page.search_posts(keyword)\nprojects/byblog/pages/common_component.py:9: in search_posts\n    self.element(\"search_input\").clear_then_input_value(text)\ncommon/elements/input.py:13: in clear_then_input_value\n    self._behavior.clear_and_send_keys(value, self.locator)\ncommon/behaviors/web_behaviors.py:223: in clear_and_send_keys\n    self.clear(locator, *args)\ncommon/behaviors/web_behaviors.py:205: in clear\n    element = self.wait_until_visibility_of_element(locator, *args)\ncommon/behaviors/web_behaviors.py:124: in wait_until_visibility_of_element\n    return self.until(EC.visibility_of_element_located((by, value)), message)\nvenv/lib/python3.6/site-packages/selenium/webdriver/support/wait.py:80: in until\n    raise TimeoutException(message, screen, stacktrace)\nE   selenium.common.exceptions.TimeoutException: Message: Unable to get the element to be visible by name: \"q\" in the page \"https://www.baidu.com/\"', '/projects/byblog/test_reports/screenshots/20191027120609202119.png', NULL, 'fail', NULL, '2019-10-27 04:07:34', '2019-10-27 04:07:34'),
(15, 10, 3, NULL, NULL, NULL, 'pass', NULL, '2019-10-27 04:10:50', '2019-10-27 04:10:50');

-- --------------------------------------------------------

--
-- Table structure for table `test_environment`
--

CREATE TABLE `test_environment` (
  `id` int NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `test_environment`
--

INSERT INTO `test_environment` (`id`, `name`) VALUES
(1, 'INT'),
(2, 'QA'),
(3, 'Regression'),
(4, 'Staging'),
(5, 'Production');

-- --------------------------------------------------------

--
-- Table structure for table `test_function`
--

CREATE TABLE `test_function` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `script_id` int NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `test_function`
--

INSERT INTO `test_function` (`id`, `name`, `script_id`, `update_time`) VALUES
(1, 'test_post_comment_amount_0', 1, '2019-10-27 03:50:00'),
(2, 'test_post_comment_amount_1', 1, '2019-10-27 03:50:04'),
(3, 'test_post_comment_amount_2', 1, '2019-10-27 03:50:08'),
(4, 'test_posts_amount', 2, '2019-10-27 03:50:13'),
(5, 'test_create_new_post', 2, '2019-10-27 03:50:17'),
(6, 'test_sort_posts_only_available_for_logged_in_user', 3, '2019-10-27 04:07:07'),
(7, 'test_view_posts_when_jump_page', 4, '2019-10-27 04:07:12'),
(8, 'test_post_id_in_detail_page_url', 4, '2019-10-27 04:07:16'),
(9, 'test_view_posts_in_search_result', 4, '2019-10-27 04:07:20'),
(10, 'test_view_posts_in_search_result', 5, '2019-10-27 04:10:34');

-- --------------------------------------------------------

--
-- Table structure for table `test_round`
--

CREATE TABLE `test_round` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `project_id` int NOT NULL,
  `test_suite_id` int NOT NULL,
  `browser_id` int DEFAULT NULL,
  `device_id` int DEFAULT NULL,
  `mobile_os_id` int DEFAULT NULL,
  `platform_os_id` int NOT NULL,
  `test_environment_id` int NOT NULL,
  `test_type_id` int NOT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `location` varchar(1000) DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `test_round`
--

INSERT INTO `test_round` (`id`, `name`, `project_id`, `test_suite_id`, `browser_id`, `device_id`, `mobile_os_id`, `platform_os_id`, `test_environment_id`, `test_type_id`, `ip`, `location`, `create_time`, `update_time`) VALUES
(1, 'Round20191027115020', 1, 1, NULL, NULL, NULL, 3, 2, 2, '117.174.131.114', 'CN,Chengdu', '2019-10-27 03:51:58', '2019-10-27 03:51:58'),
(2, 'Round20191027120723', 2, 2, 7, NULL, NULL, 3, 2, 3, '171.92.109.105', 'CN,Mianyang', '2019-10-27 04:07:29', '2019-10-27 04:07:29'),
(3, 'Round20191027121037', 3, 3, NULL, 1, 1, 3, 2, 4, '171.92.109.105', 'CN,Mianyang', '2019-10-27 04:10:49', '2019-10-27 04:10:49'),
(4, 'Round20200310142311', 2, 4, 8, NULL, NULL, 4, 2, 3, '182.149.135.130', 'CN,Zhongba', '2020-03-10 06:23:12', '2020-03-10 06:23:12'),
(5, 'Round20200321100303', 3, 5, NULL, 1, 3, 3, 2, 4, '117.174.131.113', 'CN,Chengdu', '2020-03-21 02:03:18', '2020-03-21 02:03:18'),
(6, 'Round20200321100523', 2, 6, 9, NULL, NULL, 3, 2, 3, '117.174.131.113', 'CN,Chengdu', '2020-03-21 02:05:26', '2020-03-21 02:05:26'),
(7, 'Round20200321100621', 2, 7, 9, NULL, NULL, 3, 2, 3, '117.173.212.236', 'CN,Chengdu', '2020-03-21 02:06:26', '2020-03-21 02:06:26');

-- --------------------------------------------------------

--
-- Table structure for table `test_script`
--

CREATE TABLE `test_script` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `project_id` int NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `test_script`
--

INSERT INTO `test_script` (`id`, `name`, `project_id`, `create_time`, `update_time`) VALUES
(1, 'test_post_comment', 1, '2019-10-27 03:49:59', '2019-10-27 03:49:59'),
(2, 'test_posts', 1, '2019-10-27 03:50:12', '2019-10-27 03:50:12'),
(3, 'test_permission', 2, '2019-10-27 04:07:06', '2019-10-27 04:07:06'),
(4, 'test_view_posts', 2, '2019-10-27 04:07:11', '2019-10-27 04:07:11'),
(5, 'test_view_posts', 3, '2019-10-27 04:10:33', '2019-10-27 04:10:33');

-- --------------------------------------------------------

--
-- Table structure for table `test_script_brief`
--

CREATE TABLE `test_script_brief` (
  `id` int NOT NULL,
  `script_id` int NOT NULL,
  `version` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `status` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `author` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `maintainer` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `file_created` date NOT NULL,
  `file_updated` date NOT NULL,
  `tag` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `test_suite`
--

CREATE TABLE `test_suite` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `test_suite`
--

INSERT INTO `test_suite` (`id`, `name`, `create_time`, `update_time`) VALUES
(1, 'Suite20191027114957', '2019-10-27 03:49:57', '2019-10-27 03:49:57'),
(2, 'Suite20191027120704', '2019-10-27 04:07:05', '2019-10-27 04:07:05'),
(3, 'Suite20191027121031', '2019-10-27 04:10:31', '2019-10-27 04:10:31'),
(4, 'Suite20200310142310', '2020-03-10 06:23:08', '2020-03-10 06:23:08'),
(5, 'Suite20200321100301', '2020-03-21 02:03:02', '2020-03-21 02:03:02'),
(6, 'Suite20200321100521', '2020-03-21 02:05:22', '2020-03-21 02:05:22'),
(7, 'Suite20200321100619', '2020-03-21 02:06:20', '2020-03-21 02:06:20'),
(8, 'Suite20200321100956', '2020-03-21 02:09:57', '2020-03-21 02:09:57');

-- --------------------------------------------------------

--
-- Table structure for table `test_type`
--

CREATE TABLE `test_type` (
  `id` int NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `test_type`
--

INSERT INTO `test_type` (`id`, `name`) VALUES
(1, 'UnitTest'),
(2, 'Rest'),
(3, 'Web'),
(4, 'Mobile'),
(5, 'Windows');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `browser`
--
ALTER TABLE `browser`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `case_suite`
--
ALTER TABLE `case_suite`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `device`
--
ALTER TABLE `device`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `driver`
--
ALTER TABLE `driver`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `mobile_os`
--
ALTER TABLE `mobile_os`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `platform_os`
--
ALTER TABLE `platform_os`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_case`
--
ALTER TABLE `test_case`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_case_result`
--
ALTER TABLE `test_case_result`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_environment`
--
ALTER TABLE `test_environment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_function`
--
ALTER TABLE `test_function`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_round`
--
ALTER TABLE `test_round`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_script`
--
ALTER TABLE `test_script`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_script_brief`
--
ALTER TABLE `test_script_brief`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_suite`
--
ALTER TABLE `test_suite`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `test_type`
--
ALTER TABLE `test_type`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `browser`
--
ALTER TABLE `browser`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `case_suite`
--
ALTER TABLE `case_suite`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `device`
--
ALTER TABLE `device`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `driver`
--
ALTER TABLE `driver`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `mobile_os`
--
ALTER TABLE `mobile_os`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `platform_os`
--
ALTER TABLE `platform_os`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `project`
--
ALTER TABLE `project`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `test_case`
--
ALTER TABLE `test_case`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `test_case_result`
--
ALTER TABLE `test_case_result`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `test_environment`
--
ALTER TABLE `test_environment`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `test_function`
--
ALTER TABLE `test_function`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `test_round`
--
ALTER TABLE `test_round`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `test_script`
--
ALTER TABLE `test_script`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `test_script_brief`
--
ALTER TABLE `test_script_brief`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `test_suite`
--
ALTER TABLE `test_suite`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `test_type`
--
ALTER TABLE `test_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
