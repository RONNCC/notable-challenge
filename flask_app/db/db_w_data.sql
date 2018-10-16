DROP TABLE IF EXISTS `doctors`;

CREATE TABLE `doctors` (
  `firstname` varchar(255) default NULL,
  `lastname` varchar(255) default NULL,
  `phone` varchar(100) default NULL
);

INSERT INTO `doctors` (`firstname`,`lastname`,`phone`) VALUES ("Sophia","Vasquez","363-640-5835"),("Paul","Perez","509-783-4774"),("Ora","Cunningham","942-699-8497"),("Rahim","Kent","775-155-8880"),("Anastasia","Griffith","629-462-4371"),("Sylvester","Blankenship","958-277-1412"),("Noelani","Barron","122-129-3973"),("Amaya","Cain","842-996-1089"),("Bruno","Webb","396-747-4771"),("Kyra","Faulkner","100-692-7039");

DROP TABLE IF EXISTS  `appointments`;

CREATE TABLE `appointments` (
  `appt_time` datetime,
  `kind` varchar(255) default NULL,
  `patient_id` int default NULL,
  `doctor_id` int default NULL
);

INSERT INTO `appointments` (`appt_time`,`kind`,`patient_id`,`doctor_id`) VALUES ("2018-10-11 18:34:39","New Patient",4,1),("2019-04-18 15:23:05","Follow-up",8,10),("2019-07-05 12:25:07","Follow-up",6,5),("2018-11-28 14:49:23","Follow-up",2,2),("2019-03-21 08:48:26","New Patient",6,4),("2019-09-09 18:07:20","New Patient",4,5),("2019-02-01 16:16:42","Follow-up",1,6),("2019-01-07 05:42:26","Follow-up",2,3),("2019-05-12 01:46:40","New Patient",4,5),("2019-06-28 11:37:11","New Patient",9,10);

DROP TABLE IF EXISTS `patients`;

CREATE TABLE `patients` (
  `firstname` varchar(255) default NULL,
  `lastname` varchar(255) default NULL,
  `phone` varchar(100) default NULL
);

INSERT INTO `patients` (`firstname`,`lastname`,`phone`) VALUES ("Connor","Cannon","312-500-7657"),("Lawrence","Owen","949-879-2651"),("Renee","England","263-107-1222"),("Idona","Gardner","929-273-4500"),("Colin","Shaw","231-641-5947"),("Plato","Luna","612-813-5879"),("Peter","Barnett","619-211-5493"),("India","Griffith","207-245-5631"),("Prescott","Day","151-694-0295"),("Aurelia","Glover","264-682-5618");
