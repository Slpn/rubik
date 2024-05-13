#!/bin/bash

num_runs=100

total_moves=0

for ((i=1; i<=$num_runs; i++))
do
    echo "Running iteration $i..."
    start_time=$(date +%s%N)
    echo "start" $start_time
    python3 src/main.py "U"
    output=$?
    end_time=$(date +%s%N)
    echo "e,d" $end_time
    max_duration=0.0
    echo $output
    if [ "$output" -eq -1 ]; then
        echo "The rubik is not solved"
        exit  # Quitte le script avec un code de sortie 0 (succès)
    elif [ "$output" -eq -2 ]; then
        echo "An error occurred"
        exit  # Quitte le script avec un code de sortie 0 (succès)
    fi
    duration=$(echo "$end_time - $start_time" | bc)

    # Convertir la durée en secondes avec une précision de nanoseconde


    printf "Durée d'exécution : %.9f secondes\n" "$duration"
    echo $max_duration
    if [ "$duration" -gt "$max_duration" ]; then
        max_duration="$duration"
    fi
    moves="$output" 
    total_moves=$(( $total_moves + $moves ))
    echo "Number of moves for iteration $i: $moves"
done

# Calculate average number of moves
average_moves=$(( $total_moves / $num_runs ))
echo "Average number of moves: $average_moves"
echo "Max duration: $max_duration"
