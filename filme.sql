-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 16-Jan-2022 às 22:41
-- Versão do servidor: 10.4.20-MariaDB
-- versão do PHP: 7.3.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `filme`
--
CREATE DATABASE IF NOT EXISTS `filme` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `filme`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `avaliacoes`
--

CREATE TABLE `avaliacoes` (
  `id` int(11) NOT NULL,
  `id_filme` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `nota` int(11) NOT NULL,
  `avaliacao` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `avaliacoes`
--

INSERT INTO `avaliacoes` (`id`, `id_filme`, `email`, `nota`, `avaliacao`) VALUES
(1, 2, 'karol@gmail.com', 10, 'filme incrivel'),
(2, 2, 'rafa@gmail.com', 9, 'filme legal');

-- --------------------------------------------------------

--
-- Estrutura da tabela `filmes`
--

CREATE TABLE `filmes` (
  `id` int(11) NOT NULL,
  `titulo` varchar(255) NOT NULL,
  `titulo_original` varchar(255) NOT NULL,
  `ano` int(11) NOT NULL,
  `indicacao` int(11) NOT NULL,
  `duracao` int(11) NOT NULL,
  `sinopse` text NOT NULL,
  `categoria` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `filmes`
--

INSERT INTO `filmes` (`id`, `titulo`, `titulo_original`, `ano`, `indicacao`, `duracao`, `sinopse`, `categoria`) VALUES
(2, 'Na Natureza Selvagem', 'Into the Wild', 2006, 16, 125, 'dedededede', 'bcbcbcbcbcbcbccb'),
(4, 'NO Limite do Amanhã', 'Edge of Tomorrow', 2014, 16, 113, 'Um filme de Doug Liman com Tom Cruise, Emily Blunt, Bill Paxton, Brendan Gleeson. Quando a Terra é tomada por alienígenas, Bill Cage', 'Ação'),
(5, 'Doutor Estranho', 'Doctor Strange', 2016, 16, 115, 'Após sua carreira ser destruida, um brilhante, porém, arrogante cirurgão ganha uma nova chance em sua vida quando um feiticeiro o treina para se tornar o Mago Supremo', 'Aventura'),
(6, 'Um Sonho de Liberdade', 'xx', 1994, 18, 144, 'Andy é condenado a duas prisões perpétuas consecutivas pelas mortes de sua esposa e de seu amante. Porém, só Andy sabe que não cometeu os crimes', 'Drama');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `avaliacoes`
--
ALTER TABLE `avaliacoes`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `filmes`
--
ALTER TABLE `filmes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `avaliacoes`
--
ALTER TABLE `avaliacoes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `filmes`
--
ALTER TABLE `filmes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
