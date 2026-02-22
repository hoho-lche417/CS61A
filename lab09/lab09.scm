(define (over-or-under0 num1 num2)
  (cond ((< num1 num2) -1)
    ((= num1 num2) 0)
    ((> num1 num2) 1))
)

(define (over-or-under num1 num2)
  (if (< num1 num2) -1 
    (
      if (= num1 num2) 0 1
    )
  )
)

(define (make-adder0 num)
  (lambda (inc) (+ num inc))
)

(define (make-adder num)
  (define (adder inc) (+ num inc))
  adder
)

(define (composed0 f g)
  (lambda (x) (f (g x)))
)

(define (composed f g)
  (define (func x) (f (g x))
  )
  func
)

(define (repeat0 f n) 
  (define (func x) 
    (if (= n 0) x (f ((repeat f (- n 1)) x)))
  )
  func
)

(define (repeat1 f n)
  (lambda (x) 
    (if (= n 0) x 
      ((composed f (repeat f (- n 1))) x)
    )
  )
)

(define (repeat f n)
  (if (= n 0) (lambda (x) x)
    (composed f (repeat f (- n 1)))
  )
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (if (zero? (modulo (max a b) (min a b)))
    (min a b)
    (gcd (min a b) (modulo (max a b) (min a b)))
  )
)



