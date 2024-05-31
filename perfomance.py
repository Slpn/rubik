import subprocess
import time
from tqdm import tqdm

SCRIPT = "python src/main.py --generate 10"
ITER = 50


try:
    max_duration = 0
    total_mouves = 0
    process = None
    for _ in tqdm(range(ITER)):

        start_time = time.time()
        process = subprocess.run(
            SCRIPT, shell=True, capture_output=True, text=True, check=True)
        end_time = time.time()

        return_value = process.returncode

        mouves = process.stdout.split()

        total_mouves += len(mouves)
        execution_time = end_time - start_time
        if execution_time > max_duration:
            max_duration = execution_time
        # print('Spins:', len(mouves))
        # print('Time:', round(execution_time, 2), 'seconds')

    print()
    print('Average number of spins:', int(total_mouves / ITER))
    print('Max duration time:', round(max_duration, 2), " seconds")

except subprocess.CalledProcessError as e:
    print(process.stdout)
    print(f"Erreur lors de l'exécution : {e.stderr}")


except KeyboardInterrupt:
    print("Canceled")
