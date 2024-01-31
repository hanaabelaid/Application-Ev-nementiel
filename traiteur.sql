-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : lun. 29 jan. 2024 à 15:18
-- Version du serveur :  10.4.18-MariaDB
-- Version de PHP : 8.0.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `traiteur`
--

-- --------------------------------------------------------

--
-- Structure de la table `client`
--

CREATE TABLE `client` (
  `CNE` varchar(20) NOT NULL,
  `nom` varchar(20) DEFAULT NULL,
  `prenom` varchar(20) DEFAULT NULL,
  `tele` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `type_event` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `client`
--

INSERT INTO `client` (`CNE`, `nom`, `prenom`, `tele`, `email`, `type_event`, `date`) VALUES
('12345', 'belaid', 'hanaa', '0636279764', 'hanaabelaid@gmail.co', 'buffet', '2024-01-11'),
('2345', 'test', 'test', '078654678', 'test@', 'annivarsaire', '2024-09-11'),
('5446', 'test2', 'test5', '6830603', 'test22@', 'annivarsaire', '2024-09-11'),
('987654', ' fatmi', 'firdaouss', '0677552155', 'fatmi@gmail.com', 'buffet', '2000-03-23'),
('CNE1', 'Martin', 'Sophie', '111111', 'sophie.martin@exampl', 'buffet', '2024-01-15'),
('CNE10', 'Moreau', 'Noah', '101010', 'noah.moreau@example.', 'table', '2024-10-21'),
('CNE11', 'Lemoine', 'Charlotte', '404040', 'charlotte.lemoine@ex', 'table', '2024-10-05'),
('CNE12', 'Leroy', 'Maxime', '222222', 'maxime.leroy@example', 'table', '2024-12-20'),
('CNE13', 'Dufour', 'Olivier', '333333', 'olivier.dufour@examp', 'buffet', '2024-01-10'),
('CNE14', 'Legrand', 'Juliette', '444444', 'juliette.legrand@exa', 'table', '2024-02-05'),
('CNE15', 'Garnier', 'Antoine', '555555', 'antoine.garnier@exam', 'buffet', '2024-03-18'),
('CNE16', 'Roux', 'Clémence', '666666', 'clemence.roux@exampl', 'table', '2024-04-12'),
('CNE17', 'Bertrand', 'Lucas', '777777', 'lucas.bertrand@examp', 'buffet', '2024-05-24'),
('CNE18', 'Picard', 'Chloé', '888888', 'chloe.picard@example', 'table', '2024-06-09'),
('CNE19', 'Lemoine', 'Théo', '999999', 'theo.lemoine@example', 'buffet', '2024-07-15'),
('CNE2', 'Lefevre', 'Thomas', '222222', 'thomas.lefevre@examp', 'table', '2024-02-20'),
('CNE20', 'Muller', 'Laura', '101010', 'laura.muller@example', 'table', '2024-08-21'),
('CNE21', 'Martinez', 'Aurélie', '111111', 'aurelie.martinez@exa', 'buffet', '2024-11-15'),
('CNE3', 'Dubois', 'Camille', '333333', 'camille.dubois@examp', 'buffet', '2024-03-10'),
('CNE4', 'Laurent', 'Lucas', '444444', 'lucas.laurent@exampl', 'table', '2024-04-05'),
('CNE5', 'Girard', 'Emma', '555555', 'emma.girard@example.', 'buffet', '2024-05-18'),
('CNE6', 'Thomas', 'Hugo', '666666', 'hugo.thomas@example.', 'table', '2024-06-12'),
('CNE7', 'Robert', 'Louise', '777777', 'louise.robert@exampl', 'buffet', '2024-07-24'),
('CNE8', 'Fournier', 'Arthur', '888888', 'arthur.fournier@exam', 'table', '2024-08-09'),
('CNE9', 'Dupont', 'Léa', '999999', 'lea.dupont@example.c', 'buffet', '2024-09-15'),
('D1300157', 'AMINA', 'LKHOYALI', '098764323', 'aminalkhoyali@gmail.', 'table', '2024-12-23');

-- --------------------------------------------------------

--
-- Structure de la table `event`
--

CREATE TABLE `event` (
  `type_event` varchar(20) NOT NULL,
  `prix` int(11) DEFAULT NULL,
  `descrip` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `event`
--

INSERT INTO `event` (`type_event`, `prix`, `descrip`) VALUES
('annivarsaire', 100, '.'),
('buffet', 200, 'descri'),
('buffet2', 400, '.'),
('table', 300, 'descrip2');

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

CREATE TABLE `utilisateur` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`username`, `password`) VALUES
('utilisateur', 'motdepasse'),
('user', 'user1');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`CNE`),
  ADD KEY `type_event` (`type_event`);

--
-- Index pour la table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`type_event`);

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `client`
--
ALTER TABLE `client`
  ADD CONSTRAINT `client_ibfk_1` FOREIGN KEY (`type_event`) REFERENCES `event` (`type_event`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
