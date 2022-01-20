#!groovy

final int TEST_TIMEOUT_SECS = 20
Map groups = [:]
int stagesTried = 0
int stagesSuccessful = 0

stage('Init') {
    node {
        cleanWs()
        checkout scm
        List exercises = sh(script: 'for f in ovn????; do [[ -d $f && ! -f $f/skip.txt ]] && echo $f; done', returnStdout: true).split()
        groups = exercises.groupBy { it.take(5) }
        echo "Exercise groups: ${groups.keySet()}"

        String schedule = 'jenkins-schedule.txt'
        if (fileExists(schedule)) {
            List listedExercises = readFile(schedule).readLines().findResults {
                String line = it.trim()
                (line && !line.startsWith('#')) ? line : null
            }
            echo "Listed exercise groups: ${listedExercises}"
            groups = groups.subMap(listedExercises)
            echo "Will run ${groups.keySet()}"
        }
    }
}

Closure runPython = { testDir ->
    stage(testDir) {
        node {
            cleanWs()
            checkout scm
            echo "Running test ${testDir}"
            timeout(time: TEST_TIMEOUT_SECS, unit: 'SECONDS') {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    ++stagesTried
                    dir(testDir) {
                        sh "python3 -m pytest . -vx"
                    }
                    ++stagesSuccessful
                }
            }
        }
    }
}

groups.each { k, v ->
    Map stages = v.collectEntries { ovn ->
        [ovn, runPython.curry(ovn)]
    }
    parallel stages

    // Unless all stages were successful, we should mark the build as failed.
    echo "Successful stages: ${stagesSuccessful}/${stagesTried}"
    if (stagesSuccessful < stagesTried) {
        currentBuild.result = 'FAILURE'
    }
}
