; Scheme solution by Andreas Pauley

(define a '(1 2 3 4 5))
(map + (cdr a) (reverse (cdr (reverse a))))
