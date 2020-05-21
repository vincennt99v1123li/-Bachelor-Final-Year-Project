-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 21, 2020 at 05:38 PM
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
  `course_name` char(50) NOT NULL,
  `staff_id` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course`
--

INSERT INTO `course` (`course_id`, `course_name`, `staff_id`) VALUES
(1, 'A (Tut)(G1)', 124),
(2, 'A (Lec)', 124),
(3, 'A (Tut)(G2)', 125),
(4, 'D', 124),
(5, 'E', 125),
(6, 'F', 125),
(7, 'G', 125),
(8, 'Final Year Project', 125),
(10, 'Chinese', 124),
(11, 'Engilsh', 125),
(12, 'Project Management', 124);

-- --------------------------------------------------------

--
-- Table structure for table `course_timetable`
--

CREATE TABLE `course_timetable` (
  `time_table_id` int(10) NOT NULL,
  `course_id` int(10) NOT NULL,
  `day` char(10) NOT NULL,
  `time` char(10) NOT NULL,
  `room` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `course_timetable`
--

INSERT INTO `course_timetable` (`time_table_id`, `course_id`, `day`, `time`, `room`) VALUES
(1, 1, '28-4-2020', '11:30', '1034'),
(2, 2, '28-4-2020', '13:00', '103'),
(3, 2, '12-3-2020', '11:30', '123'),
(4, 2, '5-5-2020', '12:00', '101'),
(5, 2, '3-1-2021', '08:30', '197'),
(6, 1, '7-5-2020', '12:40', '129'),
(7, 2, '5-7-2020', '11:30', '121'),
(8, 2, '7-5-2020', '11:30', '121'),
(9, 2, '5-6-2020', '11:00', '123'),
(10, 8, '5-7-2020', '15:00', '202'),
(11, 11, '10-5-2020', '12:00', '123'),
(12, 1, '22-8-2020', '12:00', '101'),
(13, 2, '11-8-2020', '13:00', '142'),
(14, 2, '15-5-2020', '16:00', '107');

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
(101, '2020-04-30 21:49:38.921620', 66, 2),
(102, '2020-05-03 00:11:07.685656', 67, 2),
(103, '2020-05-05 00:24:06.783712', 68, 4),
(101, '2020-05-07 00:18:34.308211', 69, 6),
(101, '2020-05-07 16:23:35.245530', 70, 8),
(101, '2020-05-07 21:50:03.206862', 71, 7),
(101, '2020-05-07 21:50:15.271884', 72, 7),
(101, '2020-05-07 21:56:50.117945', 73, 8),
(101, '2020-05-08 16:31:48.924738', 74, 7),
(101, '2020-05-10 21:19:50.867810', 75, 8),
(103, '2020-05-11 15:00:03.934369', 76, 8),
(103, '2020-05-11 15:01:00.627851', 77, 8),
(104, '2020-05-15 15:36:36.523987', 78, 6),
(101, '2020-05-15 15:45:40.881383', 79, 14);

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staff_id` int(100) NOT NULL,
  `password` char(10) NOT NULL,
  `first_name` char(50) NOT NULL,
  `last_name` char(10) NOT NULL,
  `position` char(10) NOT NULL,
  `sex` char(1) NOT NULL,
  `date_of_birth` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staff_id`, `password`, `first_name`, `last_name`, `position`, `sex`, `date_of_birth`) VALUES
(123, '123', 'Vin2', 'Li', 'Admin', 'M', '23-11-1999'),
(124, '123', 'PandaEric', 'Poon', 'Teacher', 'M', '23-2-1999'),
(125, '246', 'Pak', 'Wong', 'Teacher', 'M', '23-1-1990'),
(126, '123', 'm.mky', 'Ma', 'Officer', 'F', '1-4-1999'),
(127, 'N', 'Marry', 'Chan', 'Teacher', 'F', '1-2-1999'),
(128, 'N', 'Kan', 'Chen', 'Teacher', 'F', '11-11-1991'),
(129, '123', 'Mandy', 'Wong', 'Officer', 'F', '4-4-1982');

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
  `face_train` char(1) NOT NULL,
  `password` char(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`first_name`, `last_name`, `sex`, `date_of_birth`, `student_id`, `face_cap`, `face_train`, `password`) VALUES
('Vincent', 'Li', 'M', '23-11-1999', 101, 'Y', 'Y', '123'),
('Ada', 'Chan', 'F', '28-10-1998', 102, 'Y', 'Y', '123'),
('hello3', 'Li', 'M', '23-11-1999', 103, 'Y', 'Y', '123'),
('yo', 'wong', 'F', '11-4-2000', 104, 'Y', 'Y', '123'),
('Paul', 'Wong', 'M', '3-5-1999', 112, 'N', 'N', '123'),
('Ben', 'Wong', 'M', '12-2-2000', 113, 'N', 'N', '123'),
('Paul', 'Chen', 'F', '11-11-1998', 114, 'N', 'N', '123');

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
(101, 8),
(101, 11),
(102, 2),
(102, 3),
(102, 8),
(102, 11),
(103, 1),
(103, 2),
(112, 1),
(113, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `course`
--
ALTER TABLE `course`
  ADD PRIMARY KEY (`course_id`),
  ADD KEY `staff_id` (`staff_id`);

--
-- Indexes for table `course_timetable`
--
ALTER TABLE `course_timetable`
  ADD PRIMARY KEY (`time_table_id`),
  ADD KEY `course_id` (`course_id`);

--
-- Indexes for table `login_record`
--
ALTER TABLE `login_record`
  ADD PRIMARY KEY (`login_id`),
  ADD KEY `student_id` (`student_id`,`time_table_id`),
  ADD KEY `time_table_id` (`time_table_id`);

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
-- Indexes for table `student_course`
--
ALTER TABLE `student_course`
  ADD KEY `student_id` (`student_id`,`course_id`),
  ADD KEY `course_id` (`course_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `course`
--
ALTER TABLE `course`
  MODIFY `course_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `course_timetable`
--
ALTER TABLE `course_timetable`
  MODIFY `time_table_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `login_record`
--
ALTER TABLE `login_record`
  MODIFY `login_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=80;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staff_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=130;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `student_id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=116;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `course`
--
ALTER TABLE `course`
  ADD CONSTRAINT `course_ibfk_1` FOREIGN KEY (`staff_id`) REFERENCES `staff` (`staff_id`);

--
-- Constraints for table `course_timetable`
--
ALTER TABLE `course_timetable`
  ADD CONSTRAINT `course_timetable_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);

--
-- Constraints for table `login_record`
--
ALTER TABLE `login_record`
  ADD CONSTRAINT `login_record_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  ADD CONSTRAINT `login_record_ibfk_2` FOREIGN KEY (`time_table_id`) REFERENCES `course_timetable` (`time_table_id`);

--
-- Constraints for table `student_course`
--
ALTER TABLE `student_course`
  ADD CONSTRAINT `student_course_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  ADD CONSTRAINT `student_course_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
