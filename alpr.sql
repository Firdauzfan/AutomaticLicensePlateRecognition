-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Aug 23, 2018 at 06:05 PM
-- Server version: 5.7.23-0ubuntu0.18.04.1
-- PHP Version: 7.2.9-1+ubuntu16.04.1+deb.sury.org+1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alpr`
--

-- --------------------------------------------------------

--
-- Table structure for table `backup_track_plat`
--

CREATE TABLE `backup_track_plat` (
  `id_track` int(5) NOT NULL,
  `plat_no` varchar(10) NOT NULL,
  `waktu` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pengguna`
--

CREATE TABLE `pengguna` (
  `id_pengguna` int(5) NOT NULL,
  `nama_pengguna` varchar(15) NOT NULL,
  `nip` int(5) NOT NULL,
  `unit` varchar(10) NOT NULL,
  `jenis_kelamin` char(1) NOT NULL,
  `tanda_aktif` enum('1','0','','') NOT NULL,
  `tanda_dihapus` enum('1','0','','') NOT NULL,
  `tanggal_dibuat` datetime NOT NULL,
  `tanggal_dihapus` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `pengguna`
--

INSERT INTO `pengguna` (`id_pengguna`, `nama_pengguna`, `nip`, `unit`, `jenis_kelamin`, `tanda_aktif`, `tanda_dihapus`, `tanggal_dibuat`, `tanggal_dihapus`) VALUES
(1, 'Firdauz Fanani', 12345, 'IT', 'L', '1', '0', '2018-01-15 00:00:00', '0000-00-00 00:00:00'),
(2, 'Chandra', 12345, 'IT', 'L', '1', '0', '2018-01-15 00:00:00', '2018-01-15 00:00:00'),
(3, 'Fanani', 54321, 'IT', 'L', '1', '0', '2018-01-16 00:00:00', '2018-01-16 09:28:17');

-- --------------------------------------------------------

--
-- Table structure for table `plat_nomor`
--

CREATE TABLE `plat_nomor` (
  `id_plat` int(5) NOT NULL,
  `text_plat` varchar(10) NOT NULL,
  `kepunyaan` int(10) NOT NULL,
  `tanggal_dibuat` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `plat_nomor`
--

INSERT INTO `plat_nomor` (`id_plat`, `text_plat`, `kepunyaan`, `tanggal_dibuat`) VALUES
(1, 'AB1895KA', 1, '2018-01-15 00:00:00'),
(2, 'D5161JX', 2, '2018-01-15 00:00:00'),
(3, 'B9320VUA', 3, '2018-01-16 09:29:18');

-- --------------------------------------------------------

--
-- Table structure for table `track_plat`
--

CREATE TABLE `track_plat` (
  `id_track` int(5) NOT NULL,
  `plat_no` varchar(10) NOT NULL,
  `waktu_datang` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `waktu_pergi` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `track_plat`
--

INSERT INTO `track_plat` (`id_track`, `plat_no`, `waktu_datang`, `waktu_pergi`) VALUES
(27, 'B9320VUA', '2018-08-23 17:30:31', '2018-08-23 17:35:28');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pengguna`
--
ALTER TABLE `pengguna`
  ADD PRIMARY KEY (`id_pengguna`);

--
-- Indexes for table `plat_nomor`
--
ALTER TABLE `plat_nomor`
  ADD PRIMARY KEY (`id_plat`);

--
-- Indexes for table `track_plat`
--
ALTER TABLE `track_plat`
  ADD PRIMARY KEY (`id_track`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pengguna`
--
ALTER TABLE `pengguna`
  MODIFY `id_pengguna` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `plat_nomor`
--
ALTER TABLE `plat_nomor`
  MODIFY `id_plat` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `track_plat`
--
ALTER TABLE `track_plat`
  MODIFY `id_track` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
