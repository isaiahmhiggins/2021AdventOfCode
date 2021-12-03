BEGIN {
    up = 0
    down = 0
    forward = 0
    };
$1 == "forward" { forward = forward + $2}
$1 == "down" { down = down + $2}
$1 == "up" { up = up - $2}

END {
    depth = up + down;
    print depth;
    print forward;
    print depth * forward
}
