-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 07, 2020 at 12:52 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `flask`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(100) NOT NULL,
  `message` text NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`sno`, `name`, `email`, `message`, `phone_number`, `date`) VALUES
(2, 'Divyanshu Shekhar', 'imdshekhar@gmail.com', 'Hello Bro', '1234567890', '2020-03-06 13:28:16'),
(3, 'Divyanshu Shekhar', 'idshelloworld@gmail.com', 'Hello how are you?', '1234567890', '2020-03-06 13:34:49'),
(5, 'ids17', 'test@gmail.com', 'asdf', '1234567890', '2020-03-06 13:58:12'),
(6, 'Hello', 'test@gmail.com', 'Testing', '1234567890', '2020-03-06 14:51:38'),
(7, 'Hello', 'test@gmail.com', 'Testing', '1234567890', '2020-03-06 14:52:12');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `subtitle` text NOT NULL,
  `content` text NOT NULL,
  `slug` varchar(50) NOT NULL,
  `img_url` varchar(100) NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`sno`, `title`, `subtitle`, `content`, `slug`, `img_url`, `date`) VALUES
(1, 'first', 'first', 'first post sir ji', 'first', 'robot.jpg', '2020-03-07 15:06:18'),
(2, 'This is Second Post.', 'This is Tagline.', 'Are you Enjoying my Posts. This is Just for Testing Purpose. Good Luck.', 'second-post', 'robot.jpg', '2020-03-06 16:19:23'),
(3, 'This is Third Post.', 'This is Tagline.', 'This is Third Post.This is Third Post.This is Third Post.This is Third Post.This is Third Post.', 'third-post', 'home-bg.jpg', '2020-03-06 16:20:49'),
(4, 'This is 4th Post.', 'This is Tagline.', 'This is fourth Post.', 'fourth-post', 'about-bg.jpg', '2020-03-06 16:20:49'),
(5, 'This is Fifth Post.', 'This is Tagline.', 'This is Fifth Post.', 'fifth-post', 'nature.jpg', '2020-03-06 16:21:45'),
(6, 'This is sixth post.', 'This is Tagline.', 'This is 6th Post. Hope you Enjoy.', 'sixth-post', 'robot.jpg', '2020-03-07 13:46:26'),
(7, 'This is Seventh Post.', 'This is Tagline.', 'seventh', 'seven', 'nature.jpg', '2020-03-07 13:53:38');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
