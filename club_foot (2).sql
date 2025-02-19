-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le :  mer. 19 fév. 2025 à 19:29
-- Version du serveur :  10.1.38-MariaDB
-- Version de PHP :  7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `club_foot`
--

-- --------------------------------------------------------

--
-- Structure de la table `compta`
--

CREATE TABLE `compta` (
  `id` int(11) NOT NULL,
  `id_inscrit` int(11) DEFAULT NULL,
  `nom` varchar(255) DEFAULT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `mensualite` decimal(10,2) DEFAULT NULL,
  `date_paiement` date DEFAULT NULL,
  `mois_paye` varchar(255) DEFAULT NULL,
  `moyen_paiement` varchar(255) DEFAULT NULL,
  `retard_paiement` tinyint(1) DEFAULT NULL,
  `alerte` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `compta`
--

INSERT INTO `compta` (`id`, `id_inscrit`, `nom`, `prenom`, `mensualite`, `date_paiement`, `mois_paye`, `moyen_paiement`, `retard_paiement`, `alerte`) VALUES
(1, 13, 'vvvv', 'ccc', '150.00', '2024-06-06', 'juin', 'espece', NULL, NULL),
(3, 17, 'ali', 'tazi', '124.00', '2024-06-09', 'rrr', 'espece', 1, 1),
(5, 11, 'wer', 'tyu', '140.00', '2024-11-11', 'dddd', 'espece', 0, 0);

-- --------------------------------------------------------

--
-- Structure de la table `inscrits`
--

CREATE TABLE `inscrits` (
  `id` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `photo` varchar(255) NOT NULL,
  `date_naissance` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `inscrits`
--

INSERT INTO `inscrits` (`id`, `nom`, `prenom`, `age`, `email`, `photo`, `date_naissance`) VALUES
(7, 'tre', 'qwe', 12, 'dddd', 'C:/Users/faatal/Pictures/bmw.png', '2012-02-01'),
(11, 'wer', 'tyu', 12, 'asdf', 'C:/Users/faatal/Pictures/logo-fsi-2023.png', '2011-11-11'),
(13, 'vvvv', 'ccc', 14, 'ffdff', 'C:/Users/faatal/Pictures/resto-rgm.png', '2010-05-05'),
(14, 'rayan', 'anas', 9, 'dddd', 'C:/Users/faatal/Pictures/resto-golf.png', '2014-11-03'),
(15, 'ranyan', 'uio', 15, 'ffgdg', 'C:/Users/faatal/Pictures/sagim-ecole.png', '2009-05-10'),
(16, 'hassan', 'tata', 8, 'dffdf', 'C:/Users/faatal/Documents/energie solaire.png', '2016-04-09'),
(17, 'ali', 'tazi', 4, 'fggfdg', 'C:/Users/faatal/Pictures/Jnane zitoune point dacces/passe wifi.png', '2019-10-10');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `compta`
--
ALTER TABLE `compta`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_inscrit` (`id_inscrit`);

--
-- Index pour la table `inscrits`
--
ALTER TABLE `inscrits`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `compta`
--
ALTER TABLE `compta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `inscrits`
--
ALTER TABLE `inscrits`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `compta`
--
ALTER TABLE `compta`
  ADD CONSTRAINT `compta_ibfk_1` FOREIGN KEY (`id_inscrit`) REFERENCES `inscrits` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
