(defrule Malaria
  (disease_is Malaria)
  =>
  (printout t "Malaria" crlf)
)

(defrule is_it_Malaria
  (has_symptom chills)
  (has_symptom vomiting)
  (has_symptom high_fever)
  (has_symptom sweating)
  =>
  (assert (disease_is Malaria))
)

(defrule Typhoid
  (disease_is Typhoid)
  =>
  (printout t "Typhoid" crlf)
)

(defrule is_it_Typhoid
  (has_symptom chills)
  (has_symptom vomiting)
  (has_symptom fatigue)
  (has_symptom high_fever)
  =>
  (assert (disease_is Typhoid))
)

(defrule Tuberculosis
  (disease_is Tuberculosis)
  =>
  (printout t "Tuberculosis" crlf)
)

(defrule is_it_Tuberculosis
  (has_symptom chills)
  (has_symptom vomiting)
  (has_symptom fatigue)
  (has_symptom weight_loss)
  =>
  (assert (disease_is Tuberculosis))
)