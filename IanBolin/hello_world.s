# link with "gcc -o hello_world hello_world.s -nostdlib -static -Wl,--gc-sections" - 4824 bytes vs 16000 for the c++ program
	.intel_syntax noprefix

# program text
.text

	# put data in text to save size...
.LC0:
	.string	"hello_world\n"
	
.globl _start
_start:
	# don't bother with a stack, we don't use one
	# fd 1 = stdout
	mov rdi, 1
	# string pointer
	lea	rsi, .LC0[rip]
	# array length
	mov rdx, 12
	# syscall 1 (write)
	mov rax, 1
	syscall
	# return value 0
	mov rdi, 0
	# syscall 60 (exit)
	mov rax, 60
	syscall
