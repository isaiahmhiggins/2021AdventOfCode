BEGIN {
    aim = 0
    depth = 0
    forward = 0
    };
$1 == "forward" { forward = forward + $2
                  depth += aim * $2}
$1 == "down" { aim += $2; print aim}
$1 == "up" { aim -= $2; print aim}

END {
    print depth;
    print forward;
    print depth * forward
}