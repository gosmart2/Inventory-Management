-- phpMyAdmin SQL Dump
-- version 3.4.5
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Sep 25, 2020 at 06:03 PM
-- Server version: 5.5.16
-- PHP Version: 5.3.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE IF NOT EXISTS `location` (
  `location_id` int(10) NOT NULL,
  `location_name` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `location`
--

INSERT INTO `location` (`location_id`, `location_name`) VALUES
(1, 'chennai'),
(2, 'mumbai'),
(3, 'kolkata'),
(4, 'delhi');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `user` varchar(20) NOT NULL,
  `pass` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`user`, `pass`) VALUES
('gokul', 'smart');

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE IF NOT EXISTS `product` (
  `product_id` int(20) NOT NULL,
  `product_name` varchar(20) NOT NULL,
  `place` varchar(30) NOT NULL,
  `qty` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`product_id`, `product_name`, `place`, `qty`) VALUES
(1, 'bat', 'chennai', 8),
(2, 'ball', 'chennai', 35),
(3, 'stump', 'chennai', 48),
(4, 'Glove', 'chennai', 70),
(1, 'bat', 'mumbai ', 38),
(2, 'ball', 'mumbai ', 28),
(3, 'stump', 'mumbai ', 48),
(4, 'Glove', 'mumbai ', 80),
(1, 'bat', 'kolkata ', 27),
(2, 'ball', 'kolkata ', 50),
(3, 'stump', 'kolkata ', 18),
(4, 'Glove', 'kolkata ', 0),
(1, 'bat', 'delhi ', 40),
(2, 'ball', 'delhi ', 38),
(3, 'stump', 'delhi ', 17),
(4, 'Glove', 'delhi ', 36);

-- --------------------------------------------------------

--
-- Table structure for table `product_movement`
--

CREATE TABLE IF NOT EXISTS `product_movement` (
  `movementid` int(20) NOT NULL AUTO_INCREMENT,
  `timestamp` date NOT NULL,
  `from_location` varchar(40) NOT NULL,
  `to_location` varchar(40) NOT NULL,
  `product_id` int(20) NOT NULL,
  `qty` int(20) NOT NULL,
  PRIMARY KEY (`movementid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=21 ;

--
-- Dumping data for table `product_movement`
--

INSERT INTO `product_movement` (`movementid`, `timestamp`, `from_location`, `to_location`, `product_id`, `qty`) VALUES
(1, '2020-09-25', 'chennai ', 'mumbai ', 1, 20),
(2, '2020-09-25', 'mumbai ', 'kolkata ', 2, 50),
(3, '2020-09-25', 'chennai ', 'mumbai ', 3, 12),
(4, '2020-09-25', 'delhi ', 'kolkata ', 4, 22),
(5, '2020-09-25', 'chennai ', 'kolkata ', 2, 15),
(6, '2020-09-25', 'kolkata ', 'chennai ', 1, 33),
(7, '2020-09-25', 'kolkata ', 'mumbai ', 3, 10),
(8, '2020-09-25', 'chennai ', 'mumbai ', 1, 100),
(9, '2020-09-25', 'chennai ', 'mumbai ', 1, 100),
(10, '2020-09-25', 'chennai ', 'kolkata ', 1, 12),
(11, '2020-09-25', 'kolkata ', 'delhi ', 1, 40),
(12, '2020-09-25', 'delhi ', 'chennai ', 4, 12),
(13, '2020-09-25', 'delhi ', 'mumbai ', 3, 23),
(14, '2020-09-25', 'delhi ', 'mumbai ', 2, 50),
(15, '2020-09-25', 'kolkata ', 'mumbai ', 3, 12),
(16, '2020-09-25', 'mumbai ', 'kolkata ', 2, 22),
(17, '2020-09-25', 'kolkata ', 'chennai ', 4, 50),
(18, '2020-09-25', 'delhi ', 'chennai ', 2, 12),
(19, '2020-09-25', 'mumbai ', 'chennai ', 3, 12),
(20, '2020-09-25', 'mumbai ', 'kolkata ', 1, 12);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
