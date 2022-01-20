# pythonkurs

Detta repo innehåller dokumentation, övningar och tester för kursen Programmering
med Python.

## Jenkins pipeline ##

När du skapar en branch i detta repo så kommer ett motsvarande Jenkins-jobb
att skapas och byggas automatiskt. För varje push triggas ett nytt bygge i
Jenkins. När branchen tas bort tas också motsvarande Jenkins-jobb bort.

Jenkins URL:
https://devojenkins.pensionsmyndigheten.se/

Jenkins URL med Blue Ocean (rekommenderas):
https://devojenkins.pensionsmyndigheten.se/blue/organizations/jenkins/pipelines

Pipelinen kommer att försöka bygga alla övningar i repot, dvs alla kataloger med namn som matchar *ovn????*.

### Välja vilka övningar som ska köras ###

Om det finns en fil som heter **jenkins-schedule.txt** så kommer endast de grupper som finns listade i filen att köras. Övningarna grupperas ovn03, ovn04 etc.

Om du vill skippa en enstaka övning kan du skapa en fil med namnet **skip.txt** i den katalogen. Exempel:

    touch ovn0301/skip.txt
    git add ovn0301/skip.txt

osv.
# python-kurs-2019
