-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3308:3308
-- Waktu pembuatan: 16 Jan 2024 pada 17.40
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alpro_pengiriman_barang`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `customer`
--

CREATE TABLE `customer` (
  `id_customer` int(15) NOT NULL,
  `nama_customer` varchar(100) NOT NULL,
  `alamat_customer` varchar(150) NOT NULL,
  `telp_customer` varchar(14) NOT NULL,
  `email_customer` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `customer`
--

INSERT INTO `customer` (`id_customer`, `nama_customer`, `alamat_customer`, `telp_customer`, `email_customer`) VALUES
(1, 'Vilson', 'Jl. Ketapang Kepulauan Riau', '082299887564', 'vilson@gmail.com'),
(2, 'William', 'Jl. Lala Jakarta', '082299887334', 'will@gmail.com'),
(3, 'Matthew', 'Jl. haha depok', '082247687564', 'mattt@gmail.com'),
(4, 'fefw', 'ffghdh', '45353', 'dhkkng'),
(6, 'efwfwf', 'sdfsfs', '242442', 'sfsfsf'),
(7, 'rferfer', 'bdfbf', '53534', 'jmhjmjh'),
(8, 'rferfer', 'bdfbf', '53534', 'jmhjmjh'),
(9, 'grhgn', 'bfbbf', '353654', 'bdhgn'),
(10, 'grhgn', 'bfbbf', '353654', 'bdhgn'),
(11, 'grhgn', 'bfbbf', '353654', 'bdhgn'),
(12, 'fgghnghm', 'nvsjv', '75272', 'dsnfjs'),
(13, 'fgghnghm', 'nvsjv', '75272', 'dsnfjs'),
(14, 'fgghnghm', 'nvsjv', '75272', 'dsnfjs'),
(15, 'dfsfsg', 'fgfhkk', '342342', 'msdcmsd'),
(16, 'dfsfsg', 'fgfhkk', '342342', 'msdcmsd'),
(17, 'jdjad', 'bakdsk', '853784', 'veowie'),
(18, 'Jesslyn', 'Jl.Ketapang', '0812843756378', 'jesslyn@gmail.com'),
(19, 'Welliam', 'Jl.sebong', '082374659388', 'welliam@gmail.com'),
(20, 'Welliam', 'Jl. sebong', '0823847566', 'welliam@gmail.com'),
(21, 'welliam', 'fjkdsjkf', '234482942', 'sfksnfksf'),
(22, 'lala', 'nsdjfsfn', '94829034902', 'djsbfks'),
(23, 'lalap', 'hjsaaaa', '544242432', 'fgerhjuk'),
(24, 'lulu', 'jl.dbfjbsfs', '4242424125', 'lulu@gm'),
(25, 'Wiliiii', 'jl.wili', '0863221111', 'willii@'),
(26, 'hahi', 'jl.hahi', '08346288842', 'hah@'),
(27, 'haris', 'jl.haris', '0848247832', 'haris@gmail.com'),
(28, 'lilis', 'jl.lilis', '0874714743', 'lilis@'),
(29, 'Ason', 'jl.Aosn', '08634246234', 'ason@'),
(30, 'Bagus', 'jl.bagus', '082467324', 'bagus@'),
(31, 'njdjnasdajd', 'jl.njdjdkda', '085231635612', 'nsdnjds@'),
(32, 'dcbhsdbhjd', 'jl.dbhjddsd', '0863523324234', 'hbdshcb@'),
(33, 'marker', 'jl. marker', '08228883743', 'marker@'),
(34, 'dhebfejbf', 'dffefef', '4232422', 'efwfewfe'),
(35, 'dhbgfbhsdf', 'ndsnfnif', '0823712674124', 'vjjebgj'),
(36, 'gsfee', 'dbdbd', '3242545435', 'dvfvdv'),
(37, 'efewfefe', 'fdvfdfdb', '23443242', 'bgfbgb'),
(38, 'vieiyaa', 'jl. vieiyaa', '08636253623', 'vieyaa@'),
(39, 'Agnesss', 'haiss', '0938237283', 'agnsess@'),
(40, 'Willllll', 'yyayaya', '0742734622', 'apaan lu'),
(41, 'ddsdscs', 'fvvfdvefv', '23414324', 'fdfvdsvfdvf'),
(42, 'Vilson', 'Jl. Skc', '082288076094', 'Vilson@'),
(43, 'Vilson', 'sdfsdfs', '082288076094', 'dfgdsgdvgf'),
(44, 'Vilson', 'nfjndvaf', '082288076094', 'fvvdfvvds'),
(45, 'gergre', 'dvsvfsvf', '4525235', 'dfsvdvdv'),
(46, 'evervvre', 'dfvsdvdv', '35254', 'dvsvfdvfd'),
(47, 'haha', 'bfbfdb', '352353', 'fgbfgbgf'),
(48, 'bhjb', 'gtgrtg', '52355', 'tgrtgtr'),
(49, 'Vilson', 'jl. vilson', '08273646423', 'vilson@'),
(50, 'bhbfhberf', 'djkbfjekd', '63248467', 'bejkwbfejw'),
(51, 'Vilson', 'fdbdbbfd', '3499348', 'bfdbdbf'),
(52, 'haha', 'ishrifh', '67587', 'bjbnjkbfdv'),
(53, 'dgdg', 'fbfgbfb', '453543', 'fbgfbfbf'),
(54, 'bbuuvfdv', 'rfrefferf', '4353443', 'erffefref'),
(55, 'Vilson', 'jl.njdfsf', '84924234', 'sfsfsfdfdsf'),
(56, 'frferfrf', 'efrfref', '324342', 'referfref'),
(57, 'vilsonn', 'gdfgdgd', '34242', 'dgfdgdfg'),
(58, 'dsdfsfsdfs', 'bgdfbdfb', '2434235432', 'dfbdfbdfbfd'),
(59, 'vilson', 'jjnfjsf', '943989823', 'rrege'),
(60, 'jkefjekfes', 'dvfdvfdv', '9932432', 'dfvfdvfdv'),
(61, 'Vilsonn', 'Jl.ketapang', '082288076094', 'vilsonn@'),
(62, 'Virr', 'fsjdnfjdsfds', '08432523', 'fdsfdsfdsf'),
(63, 'ferfeferv', 'fgbfbfbfbfg', '5235345353', 'fgbfbfgbfbgf'),
(64, 'vfvdfvfdvfd', 'fbgfbf', '3542534', 'gfbfbbgfb'),
(65, 'VIlson', 'jl ahhah', '08458345', 'vislsdnk@'),
(66, 'Suhemi', 'Jl. ketapang', '0826371232', 'suhemi@gmail.com'),
(67, 'Suhemi', 'Jl. ketapang', '0826371232', 'suhemi@gmail.com'),
(68, 'Suhemi', 'Jl. ketapang', '0826371232', 'suhemi@gmail.com'),
(69, 'Suhemi', 'Jl. ketapang', '0826371232', 'suhemi@gmail.com'),
(70, 'Suhemi', 'Jl. ketapang', '0826371232', 'suhemi@gmail.com'),
(71, 'Suhemiii', 'Jl. ketapang', '0826371232', 'suhemi@gmail.com');

-- --------------------------------------------------------

--
-- Struktur dari tabel `harga_paket_oke`
--

CREATE TABLE `harga_paket_oke` (
  `id_paketoke` int(11) NOT NULL,
  `kota_asal` varchar(50) NOT NULL,
  `kota_tujuan` varchar(50) NOT NULL,
  `harga_kg` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `harga_paket_oke`
--

INSERT INTO `harga_paket_oke` (`id_paketoke`, `kota_asal`, `kota_tujuan`, `harga_kg`) VALUES
(1, 'Bandung', 'Jakarta', 5000),
(2, 'Jakarta', 'Bandung', 5000),
(3, 'Bandung', 'Batam', 10000),
(4, 'Batam', 'Bandung', 10000),
(5, 'Bandung', 'Surabaya', 7000),
(6, 'Surabaya', 'Bandung', 7000),
(7, 'Bandung', 'Semarang', 6000),
(8, 'Semarang', 'Bandung', 6000),
(9, 'Bandung', 'Bali', 9000),
(10, 'Bali', 'Bandung', 9000),
(11, 'Bandung', 'Medan', 10000),
(12, 'Medan', 'Bandung', 10000),
(13, 'Aceh', 'Bandung', 15000),
(14, 'Bandung', 'Aceh', 15000),
(15, 'Bandung', 'Kalimantan Barat', 13000),
(17, 'Kalimantan Barat', 'Bandung', 13000),
(18, 'Bandung', 'Sulawesi', 25000),
(19, 'Bandung', 'Tanjung Pinang', 20000),
(20, 'Tanjung Pinang', 'Bandung', 20000),
(21, 'Bandung', 'Depok', 6000),
(22, 'Depok', 'Bandung', 6000),
(23, 'Sulawesi', 'Bandung', 25000);

-- --------------------------------------------------------

--
-- Struktur dari tabel `harga_paket_reguler`
--

CREATE TABLE `harga_paket_reguler` (
  `id_paketreguler` int(11) NOT NULL,
  `kota_asal` varchar(50) NOT NULL,
  `kota_tujuan` varchar(50) NOT NULL,
  `harga_kg` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `harga_paket_reguler`
--

INSERT INTO `harga_paket_reguler` (`id_paketreguler`, `kota_asal`, `kota_tujuan`, `harga_kg`) VALUES
(1, 'Bandung', 'Jakarta', 7000),
(2, 'Jakarta', 'Bandung', 7000),
(3, 'Bandung', 'Batam', 12000),
(4, 'Batam', 'Bandung', 12000),
(5, 'Bandung', 'Surabaya', 9000),
(6, 'Surabaya', 'Bandung', 9000),
(7, 'Bandung', 'Semarang', 8000),
(8, 'Semarang', 'Bandung', 8000),
(9, 'Bandung', 'Bali', 11000),
(10, 'Bali', 'Bandung', 11000),
(11, 'Bandung', 'Medan', 12000),
(12, 'Medan', 'Bandung', 12000),
(14, 'Bandung', 'Depok', 8500);

-- --------------------------------------------------------

--
-- Struktur dari tabel `harga_paket_yes`
--

CREATE TABLE `harga_paket_yes` (
  `id_paketyes` int(11) NOT NULL,
  `kota_asal` varchar(50) NOT NULL,
  `kota_tujuan` varchar(50) NOT NULL,
  `harga_kg` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `harga_paket_yes`
--

INSERT INTO `harga_paket_yes` (`id_paketyes`, `kota_asal`, `kota_tujuan`, `harga_kg`) VALUES
(1, 'Bandung', 'Jakarta', 10000),
(2, 'Jakarta', 'Bandung', 10000),
(3, 'Bandung', 'Batam', 15000),
(4, 'Batam', 'Bandung', 15000),
(5, 'Bandung', 'Surabaya', 12000),
(6, 'Surabaya', 'Bandung', 12000),
(7, 'Bandung', 'Semarang', 11000),
(8, 'Semarang', 'Bandung', 11000),
(9, 'Bandung', 'Bali', 14000),
(10, 'Bali', 'Bandung', 14000),
(11, 'Bandung', 'Medan', 15000),
(12, 'Medan', 'Bandung', 15000),
(13, 'Bandung', 'Aceh', 18000),
(16, 'Aceh', 'Bandung', 18000),
(17, 'Bandung', 'Maluku', 20000),
(18, 'Maluku', 'Bandung', 20000),
(19, 'Bandung', 'NTT', 30000),
(20, 'NTT', 'Bandung', 32000),
(21, 'Bandung', 'Bogor', 11000),
(22, 'Bogor', 'Bandung', 11000);

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi_pengiriman`
--

CREATE TABLE `transaksi_pengiriman` (
  `no_resi` int(16) NOT NULL,
  `id_customer` int(15) NOT NULL,
  `tgl_transaksi` date NOT NULL,
  `jam_transaksi` time NOT NULL,
  `nama_penerima` varchar(100) NOT NULL,
  `notelp_penerima` varchar(14) NOT NULL,
  `alamat_penerima` varchar(150) NOT NULL,
  `email_penerima` varchar(50) NOT NULL,
  `nama_barang` varchar(50) NOT NULL,
  `berat_barang` float NOT NULL,
  `jenis_paket` varchar(50) NOT NULL,
  `kota_asal` varchar(100) NOT NULL,
  `kota_tujuan` varchar(100) NOT NULL,
  `metode_pembayaran` varchar(50) NOT NULL,
  `biaya_kirim` int(50) NOT NULL,
  `biaya_packing` int(50) NOT NULL,
  `biaya_asuransi` int(50) NOT NULL,
  `total` int(100) NOT NULL,
  `bayar` int(100) NOT NULL,
  `kembali` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `transaksi_pengiriman`
--

INSERT INTO `transaksi_pengiriman` (`no_resi`, `id_customer`, `tgl_transaksi`, `jam_transaksi`, `nama_penerima`, `notelp_penerima`, `alamat_penerima`, `email_penerima`, `nama_barang`, `berat_barang`, `jenis_paket`, `kota_asal`, `kota_tujuan`, `metode_pembayaran`, `biaya_kirim`, `biaya_packing`, `biaya_asuransi`, `total`, `bayar`, `kembali`) VALUES
(1, 1, '2023-06-02', '16:52:04', 'lala', '082287546372', 'jl.haha', 'lal@gmail.com', 'kursi', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 10000, 0, 20000, 30000, 50000, 20000),
(2, 17, '2023-05-12', '13:00:00', 'baba', '8349502', 'hahadked', 'yayadld', 'Hp', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 10000, 10000, 20000, 40000, 0, 0),
(3, 18, '2023-06-02', '21:36:26', 'Jolin', '082283746599', 'Jl. Lapung', 'jolin@gmail.com', 'Boneka', 2.1, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10500, 10000, 21000, 41500, 0, 0),
(4, 19, '2023-06-02', '22:28:35', 'Meli', '081234567733', 'Jl.yayay', 'meli@gmail.com', 'Iphone', 2.2, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 11000, 10000, 22000, 43000, 0, 0),
(5, 20, '2023-06-02', '22:32:36', 'Meli', '08199128374', 'Jl. yaya', 'meli@gmail.com', 'Iphone ', 2.1, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10500, 10000, 21000, 41500, 0, 0),
(6, 21, '2023-06-02', '22:36:18', 'meli', '8429423', 'sjfkjefjew', 'efkwnfk', 'iphone', 2.1, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10500, 10000, 21000, 41500, 0, 0),
(7, 22, '2023-06-04', '15:16:52', 'lili', '08326615413', 'JL.skc', 'lili@gmail.com', 'HEadphone', 2.1, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 10500, 10000, 21000, 41500, 0, 0),
(8, 23, '2023-06-04', '15:19:24', 'lilir', '8249483432', 'jl.skccc', 'lilir@', 'chager', 2.1, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 10500, 10000, 21000, 41500, 0, 0),
(9, 24, '2023-06-04', '15:25:16', 'lali', '74331345', 'jl.hjdbceb', 'lali@gma', 'HAnd', 2.1, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 10500, 10000, 21000, 41500, 0, 0),
(10, 25, '2023-06-04', '15:41:35', 'vilsss', '87392222000', 'jl.vilss', 'villss@', 'Mouse', 1.3, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 6500, 10000, 0, 16500, 0, 0),
(11, 26, '2023-06-04', '17:06:06', 'hiha', '08934276424', 'jl.hiha', 'hiha@', 'Air', 1.2, 'Paket Oke', 'Jakarta', 'Bandung', 'Cash', 6000, 10000, 12000, 28000, 0, 0),
(12, 27, '2023-06-04', '17:15:24', 'dwi', '087462832122', 'jl.dwi', 'dwi.com', 'airpods', 1, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 5000, 0, 10000, 15000, 0, 0),
(13, 28, '2023-06-04', '17:19:30', 'agnes', '087342654263', 'jl.agnes', 'agnes@', 'Jaket', 2, 'Paket Reguler', 'Bandung', 'Jakarta', 'Debit Card', 14000, 0, 0, 14000, 0, 0),
(14, 29, '2023-06-04', '17:42:28', 'Nowan', '086342643242', 'jl.nowan', 'nowan@', 'Kertas', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10000, 10000, 0, 20000, 0, 0),
(15, 30, '2023-06-04', '17:53:55', 'fauzi', '08635723434', 'jl.fauzi', 'fauzi@', 'bukuu', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10000, 10000, 20000, 40000, 0, 0),
(16, 31, '2023-06-04', '18:08:24', 'sndandjkanda', '0863515732112', 'jl. bdfjhsbfh', 'nfenifn@', 'dfuefhuefe', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10000, 10000, 20000, 40000, 0, 0),
(17, 32, '2023-06-04', '18:10:05', 'dhabbfuei', '083571235131', 'jl.dsbfhjdd', 'bfsebu@', 'vbrfuiweuf', 2, 'Paket Oke', 'Jakarta', 'Batam', 'Cash', 0, 10000, 20000, 30000, 0, 0),
(18, 33, '2023-06-04', '20:55:14', 'dori', '0863571237', 'jl. dori', 'dori@', 'dompet', 1, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 5000, 10000, 10000, 25000, 0, 0),
(19, 34, '2023-06-04', '21:08:23', 'fewfwfwf', '342424242', 'ffefwf', 'efwfwfwfe', 'efggfdgdfg', 1, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 5000, 10000, 0, 15000, 0, 0),
(20, 35, '2023-06-04', '21:15:17', 'kndneifuiewv', '0864263472', 'njdsbfjsf', 'jfbgerfer', 'dsfsgrger', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10000, 10000, 20000, 40000, 0, 0),
(21, 36, '2023-06-04', '21:17:44', 'sefevv', '353442311', 'dfvdvdb', 'vfdvfdv', 'vfddfb', 2, 'Paket Oke', 'Jakarta', 'Bandung', 'Debit Card', 10000, 10000, 20000, 40000, 0, 0),
(22, 37, '2023-06-04', '21:18:49', 'wefewfewf', '435363543', 'bgnny', 'gnrbdvd', 'dvfdvht', 3, 'Paket Reguler', 'Bandung', 'Jakarta', 'Debit Card', 21000, 0, 0, 21000, 0, 0),
(23, 38, '2023-06-05', '15:47:44', 'lulul', '08325354632', 'jl.lulu', 'lulju@gmail', 'jndsnuds', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10000, 10000, 20000, 40000, 0, 0),
(24, 39, '2023-06-05', '16:04:26', 'liann', '0932849342', 'jl. lian', 'lian@', 'bantal', 2, 'Paket Oke', 'Jakarta', 'Surabaya', 'Debit Card', 0, 10000, 20000, 30000, 0, 0),
(25, 40, '2023-06-05', '16:14:22', 'aditt', '0837472434', 'jl. adit', 'adit@', 'entah', 2.1, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10500, 10000, 21000, 41500, 0, 0),
(26, 41, '2023-06-05', '21:33:44', 'vfdvfdvdf', '23412142', 'dvsvsdfvdv', 'dvsfvdvdsv', 'ntah', 2, 'Paket Reguler', 'Bandung', 'Jakarta', 'Cash', 14000, 10000, 20000, 44000, 0, 0),
(27, 42, '2023-06-05', '21:37:31', 'William', '08236612312', 'Jl. William', 'william@', 'Komik', 2.5, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 12500, 10000, 0, 22500, 0, 0),
(28, 43, '2023-06-05', '21:44:42', 'dfvfdsvfv', '2341431452', 'dfssgvrv', 'dvsdvfdvfdv', 'sfvfvsd', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10000, 10000, 20000, 40000, 0, 0),
(29, 44, '2023-06-05', '21:48:13', 'vrevrves', '23414514', 'fdsbfdsbf', 'sbsbsgfbgb', 'sfdbdfbdb', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 10000, 0, 0, 10000, 15000, 5000),
(30, 45, '2023-06-05', '21:49:27', 'dfvdvdsvd', '324523532', 'fdbfdbg', 'fbgfdbfgb', 'fgbgbf', 3.6, 'Paket Yes', 'Jakarta', 'Batam', 'Debit Card', 0, 10000, 36000, 46000, 50000, 4000),
(31, 46, '2023-06-05', '21:52:44', 'svfvfdsvd', '34543253', 'fvsvsdfv', 'vfdsvfvfv', 'sfdvsdvf', 1.75, 'Paket Reguler', 'Jakarta', 'Surabaya', 'Debit Card', 0, 10000, 17500, 27500, 0, 0),
(32, 47, '2023-06-05', '21:58:27', 'fgbfgb', '3245235', 'bffgbfgb', 'bffbdbg', 'gergweg', 2, 'Paket Oke', 'Jakarta', 'Aceh', 'Debit Card', 0, 10000, 20000, 30000, 30000, 0),
(33, 48, '2023-06-05', '21:59:35', 'trgrtgrt', '345345', 'ggbgrtb', 'rbbrb', 'vdvfdvdv', 2, 'Paket Oke', 'Surabaya', 'Surabaya', 'Debit Card', 0, 0, 20000, 20000, 26000, 6000),
(34, 49, '2023-06-06', '10:17:29', 'mathh', '08234662432', 'jl.jdjfd', 'math@', 'remote', 1.2, 'Paket Oke', 'Bandung', 'Surabaya', 'Debit Card', 8400, 10000, 0, 18400, 20000, 1600),
(35, 50, '2023-06-06', '10:20:06', 'bdshjfed', '7423683', 'bdfheufd', 'hhadbae', 'bsdfjbfes', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10000, 10000, 20000, 40000, 0, 0),
(36, 51, '2023-06-06', '20:49:17', 'fjnjgre', '4324342', 'dfbdbd', 'dfbfdbd', 'dfgdfbdb', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Debit Card', 10000, 10000, 20000, 40000, 50000, 10000),
(37, 52, '2023-06-06', '20:53:30', 'jsdfksjf', '93249083', 'fhierhfie', 'ernfirenfi', 'fdgbdbgfd', 1, 'Paket Reguler', 'Bandung', 'Batam', 'Kredit Card', 12000, 0, 0, 12000, 12000, 0),
(38, 53, '2023-06-06', '21:19:41', 'gbfbfgb', '435435', 'ghnfbnfb', 'fgbfbfbgf', 'bdbfdbgd', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Kredit Card', 10000, 10000, 20000, 40000, 50000, 10000),
(39, 54, '2023-06-06', '21:20:38', 'ergregerger', '345435', 'grtgtr', 'grtgtrgtrg', 'fnfnfnf', 1, 'Paket Oke', 'Bandung', 'Batam', 'QRIS', 10000, 10000, 0, 20000, 30000, 10000),
(40, 55, '2023-06-06', '21:26:02', 'sdfsdf', '3432432', 'fdvvdvf', 'dfvfdvfvfd', 'fvfvfdvfd', 2, 'Paket Oke', 'Jakarta', 'Kalimantan Barat', 'Debit Card', 0, 10000, 20000, 30000, 40000, 10000),
(41, 56, '2023-06-06', '21:28:36', 'efefrefre', '433543', 'dfvfdgf', 'grgreger', 'erfefer', 1, 'Paket Yes', 'Jakarta', 'NTT', 'Debit Card', 0, 0, 0, 0, 100000, 100000),
(42, 57, '2023-06-06', '21:39:09', 'dgfdgdf', '32424234', 'dfvdfvd', 'dfvfdvfdvfdvd', 'fdsfsdfs', 2, 'Paket Reguler', 'Jakarta', 'Semarang', 'Debit Card', 0, 10000, 20000, 30000, 30000, 0),
(43, 58, '2023-06-06', '21:42:11', 'dfvfvdv', '3243233', 'dfvvdvfd', 'vfdvfdvfv', 'fvfdvfd', 2, 'Paket Reguler', 'Bandung', 'Jakarta', 'Debit Card', 14000, 10000, 20000, 44000, 45000, 1000),
(44, 59, '2023-06-07', '16:13:04', 'regregre', '432252', 'fdfbdb', 'dbfdbdbdb', 'dfbfdbfd', 2, 'Paket Reguler', 'Bandung', 'Batam', 'Debit Card', 24000, 10000, 20000, 54000, 55000, 1000),
(45, 60, '2023-06-07', '16:14:27', 'dfvfdvf', '324234', 'vfdvdfvf', 'dfvdfvfdv', 'vdvrvvr', 1, 'Paket Reguler', 'Bandung', 'Surabaya', 'Kredit Card', 9000, 10000, 10000, 29000, 30000, 1000),
(46, 61, '2023-06-12', '22:21:07', 'llalaa', '0842342342', 'jl. lala', 'lala@', 'haha', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 10000, 10000, 20000, 40000, 50000, 10000),
(47, 62, '2023-06-12', '22:23:26', 'sdfdsfsdf', '3425252', 'fsdsfsf', 'sdfsdfdsfdsf', 'dgdfgrgr', 1.2, 'Paket Yes', 'Bandung', 'Jakarta', 'Debit Card', 12000, 10000, 12000, 34000, 35000, 1000),
(48, 63, '2023-06-12', '23:11:25', 'dbsdbdbfds', '4352554', 'bgdgbfb', 'bfbfdbfgbf', 'svfdvfsdvd', 3, 'Paket Yes', 'Bandung', 'Bogor', 'Kredit Card', 33000, 10000, 30000, 73000, 80000, 7000),
(49, 64, '2023-06-12', '23:17:34', 'gfbgfbgfbg', '523523543', 'dfbfbgfb', 'fgbfbfgb', 'dfvfdvdv', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'QRIS', 10000, 10000, 0, 20000, 20000, 0),
(50, 65, '2024-01-17', '22:14:10', 'jolinn', '953985348', 'jl.yaya', 'jlon', 'hp', 2.1, 'Paket Reguler', 'Jakarta', 'Surabaya', 'Cash', 0, 0, 0, 0, 22222, 22222),
(51, 71, '2024-01-16', '23:16:44', 'Jesiccaaaaaa', '088477384', 'Jl. Jeruk', 'jesicaa@gmail.com', 'Iphone 15 pro maxx', 2, 'Paket Oke', 'Bandung', 'Jakarta', 'Cash', 10000, 10000, 20000, 40000, 50000, 10000);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id_customer`);

--
-- Indeks untuk tabel `harga_paket_oke`
--
ALTER TABLE `harga_paket_oke`
  ADD PRIMARY KEY (`id_paketoke`);

--
-- Indeks untuk tabel `harga_paket_reguler`
--
ALTER TABLE `harga_paket_reguler`
  ADD PRIMARY KEY (`id_paketreguler`);

--
-- Indeks untuk tabel `harga_paket_yes`
--
ALTER TABLE `harga_paket_yes`
  ADD PRIMARY KEY (`id_paketyes`);

--
-- Indeks untuk tabel `transaksi_pengiriman`
--
ALTER TABLE `transaksi_pengiriman`
  ADD PRIMARY KEY (`no_resi`),
  ADD KEY `fk_transaksi_pengiriman_customer` (`id_customer`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `customer`
--
ALTER TABLE `customer`
  MODIFY `id_customer` int(15) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT untuk tabel `harga_paket_oke`
--
ALTER TABLE `harga_paket_oke`
  MODIFY `id_paketoke` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT untuk tabel `harga_paket_reguler`
--
ALTER TABLE `harga_paket_reguler`
  MODIFY `id_paketreguler` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT untuk tabel `harga_paket_yes`
--
ALTER TABLE `harga_paket_yes`
  MODIFY `id_paketyes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT untuk tabel `transaksi_pengiriman`
--
ALTER TABLE `transaksi_pengiriman`
  MODIFY `no_resi` int(16) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `transaksi_pengiriman`
--
ALTER TABLE `transaksi_pengiriman`
  ADD CONSTRAINT `fk_transaksi_pengiriman_customer` FOREIGN KEY (`id_customer`) REFERENCES `customer` (`id_customer`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
