(define (ascending? s) 
    (if (or (null? s) (= (length s) 1)) #t
        (
            and (<= (car s) (car (cdr s))) (ascending? (cdr s))
        )
    )
)

(define (my-filter pred s) 
    (if (null? s) nil
        (
            append (if (pred (car s)) (list(car s)) nil) (my-filter pred (cdr s))
        )
    )
)

(define (interleave lst1 lst2) 
    (if (null? lst1) lst2
        (append (list (car lst1)) (interleave lst2 (cdr lst1)))
    )
)

(define (no-repeats s)
    (if (null? s) nil
        (append (list (car s)) (no-repeats (filter (lambda (x) (not (= x (car s)))) (cdr s))))
    )
)
