-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2020 at 04:10 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fyp`
--

-- --------------------------------------------------------

--
-- Table structure for table `course`
--

CREATE TABLE `course` (
  `course_id` int(10) NOT NULL,
  `course_name` char(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `course_name`) VALUES
(1, 'A'),
(2, 'B'),
(3, 'C'),
(4, 'D');

-- --------------------------------------------------------

--
-- Table structure for table `course_timetable`
--

CREATE TABLE `course_timetable` (
  `time_table_id` int(10) NOT NULL,
  `course_id` int(10) NOT NULL,
  `week` int(10) NOT NULL,
  `day` char(10) NOT NULL,
  `time` char(10) NOT NULL,
  `class` char(10) NOT NULL,
  `room` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course_timetable`
--

INSERT INTO `course_timetable` (`time_table_id`, `course_id`, `week`, `day`, `time`, `class`, `room`) VALUES
(1, 1, 1, '28/4/2020', '11:00', 'Lecture', '1001'),
(2, 2, 10, '28/4/2020', '13:00', 'Lecture', '103');

-- --------------------------------------------------------

--
-- Table structure for table `login_record`
--

CREATE TABLE `login_record` (
  `student_id` int(100) NOT NULL,
  `Login_date` char(50) NOT NULL,
  `login_id` int(100) NOT NULL,
  `time_table_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login_record`
--

INSERT INTO `login_record` (`student_id`, `Login_date`, `login_id`, `time_table_id`) VALUES
(101, '2020-04-28 22:28:08.594473', 49, 1),
(101, '2020-04-28 22:34:33.198431', 51, 1),
(101, '2020-04-28 22:36:09.333148', 52, 1),
(101, '2020-04-28 22:48:12.933965', 53, 1),
(101, '2020-04-28 22:56:30.793210', 54, 1),
(101, '2020-04-28 22:58:06.655563', 55, 1),
(101, '2020-04-29 00:23:37.675247', 56, 1),
(102, '2020-04-29 00:24:24.599942', 57, 1),
(101, '2020-04-29 00:26:32.453293', 58, 1),
(101, '2020-04-29 00:31:03.712399', 59, 1),
(101, '2020-04-30 15:14:55.817419', 60, 1),
(101, '2020-04-30 17:12:34.717086', 61, 1),
(101, '2020-04-30 17:12:44.647575', 62, 1),
(103, '2020-04-30 17:33:37.081180', 63, 1),
(101, '2020-04-30 21:11:54.885344', 64, 1),
(101, '2020-04-30 21:37:45.389520', 65, 1),
(101, '2020-04-30 21:49:38.921620', 66, 2);

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(100) NOT NULL,
  `username` char(10) NOT NULL,
  `password` char(10) NOT NULL,
  `first_name` char(50) NOT NULL,
  `last_name` char(10) NOT NULL,
  `position` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `username`, `password`, `first_name`, `last_name`, `position`) VALUES
(1, '123', '123', 'Eric', 'Panda', 'teacher');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `first_name` char(50) NOT NULL,
  `last_name` char(10) NOT NULL,
  `sex` char(1) NOT NULL,
  `date_of_birth` char(10) NOT NULL,
  `student_id` int(100) NOT NULL,
  `face_cap` char(1) NOT NULL,
  `face_train` char(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`first_name`, `last_name`, `sex`, `date_of_birth`, `student_id`, `face_cap`, `face_train`) VALUES
('Vincent', 'Li', 'M', '23-11-1999', 101, 'Y', 'Y'),
('Ada', 'Chan', 'F', '28-10-1998', 102, 'Y', 'Y'),
('hello', 'Li', 'M', '23-11-1999', 103, 'N', 'Y');

-- --------------------------------------------------------

--
-- Table structure for table `student_course`
--

CREATE TABLE `student_course` (
  `student_id` int(100) NOT NULL,
  `course_id` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_course`
--

INSERT INTO `student_course` (`student_id`, `course_id`) VALUES
(101, 1),
(101, 2),
(102, 2),
(102, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`);

--
-- Indexes for table `course_timetable`
--
ALTER TABLE `course_timetable`
  ADD PRIMARY KEY (`time_table_id`);

--
-- Indexes for table `login_record`
--
ALTER TABLE `login_record`
  ADD PRIMARY KEY (`login_id`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staff_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`student_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `course_timetable`
--
ALTER TABLE `course_timetable`
  MODIFY `time_table_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `login_record`
--
ALTER TABLE `login_record`
  MODIFY `login_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
