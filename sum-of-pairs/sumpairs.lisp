; Common Lisp solution by Andreas Pauley

(defvar a '(1 2 3 4 5))
(mapcar #'+ a (cdr a))
