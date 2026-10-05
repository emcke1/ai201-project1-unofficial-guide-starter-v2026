# Run log

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.7
- Runs per question: 3, caching off
- When: 2026-10-03 23:41

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question                                                                   | Run 1 | Run 2 | Run 3 |
|---                                                                         |---    |---    |---    |
| Which Physics class has the least amount of classwork?                     | fail  | fail | fail   |  
| How many credits do I need to take to declare my major?                    | fail  | fail | fail   |
| What is the university policy for snow days?                               | fail  | fail | fail   |
| How far is the university clinic from the library on campus?               | fail  | fail | fail   |
| When is it a good time go the university dining hall on a Tuesday evening? | fail  | fail | fail   |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.7. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question                                       | Best distance | Gate    |
|---                                                          |---            |---      | 
| What is the capital of Mongolia?                            | 0.825         | refused |
| How do I change the oil in a diesel engine?                 | 0.934         | refused |
| Who won the 1994 World Cup?                                 | 0.886         | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.844         | refused |
| How do I write a for loop in Rust?                          | 0.896         | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### Which Physics class has the least amount of classwork? — run 1

- Best distance: 0.5459 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_engl_205_exams.txt, course_phys_130.txt, course_phys_130_exams.txt, course_stat_150.txt

```
I do not have enough information to answer which Physics class has the least amount of classwork, as only one Physics class (PHYS 130 Mechanics) is listed in the documents. 

Source: `course_phys_130.txt` and `course_phys_130_exams.txt`
```

### Which Physics class has the least amount of classwork? — run 2

- Best distance: 0.5459 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_engl_205_exams.txt, course_phys_130.txt, course_phys_130_exams.txt, course_stat_150.txt

```
I do not have enough information to answer which Physics class has the least amount of classwork, as only one Physics class (PHYS 130 Mechanics) is listed in the documents. 

Source: course_phys_130.txt (and course_phys_130_exams.txt)
```

### Which Physics class has the least amount of classwork? — run 3

- Best distance: 0.5459 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_engl_205_exams.txt, course_phys_130.txt, course_phys_130_exams.txt, course_stat_150.txt

```
I don't have enough information to answer which Physics class has the least amount of classwork, as the documents only describe a single Physics class, PHYS 130 Mechanics. 

Source: `course_phys_130.txt` and `course_phys_130_exams.txt`
```

### How many credits do I need to take to declare my major? — run 1

- Best distance: 0.3560 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_graduation_requirements.txt, admin_pass_fail_option.txt, course_cs_340.txt

```
Based on the provided documents, there is no mention of a credit requirement needed to declare a major. You declare at the end of your second semester, or later if you need to. 

Source: `admin_declaring_a_major.txt`
```

### How many credits do I need to take to declare my major? — run 2

- Best distance: 0.3560 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_graduation_requirements.txt, admin_pass_fail_option.txt, course_cs_340.txt

```
Based on the provided documents, there is no mention of a credit requirement needed to declare a major. 

Source: `admin_declaring_a_major.txt`
```

### How many credits do I need to take to declare my major? — run 3

- Best distance: 0.3560 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_declaring_a_major.txt, admin_graduation_requirements.txt, admin_pass_fail_option.txt, course_cs_340.txt

```
Based on the provided documents, there is no mention of a credit requirement needed to declare a major. 

Source: admin_declaring_a_major.txt
```

### What is the university policy for snow days? — run 1

- Best distance: 0.5992 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_study_abroad.txt, transit_shuttle.txt, winter_gear.txt

```
I do not have enough information to answer your question.
```

### What is the university policy for snow days? — run 2

- Best distance: 0.5992 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_study_abroad.txt, transit_shuttle.txt, winter_gear.txt

```
I do not have enough information to answer your question.
```

### What is the university policy for snow days? — run 3

- Best distance: 0.5992 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_pass_fail_option.txt, admin_study_abroad.txt, transit_shuttle.txt, winter_gear.txt

```
I do not have enough information to answer your question, as the provided documents do not mention university policies for snow days.
```

### How far is the university clinic from the library on campus? — run 1

- Best distance: 0.5078 (passed the gate)
- Sources retrieved: admin_library_holds.txt, housing_aldridge_hall.txt, housing_calder_annexe_noise.txt, study_group_rooms.txt, transit_walking.txt

```
I do not have enough information to answer this question from the provided documents.
```

### How far is the university clinic from the library on campus? — run 2

- Best distance: 0.5078 (passed the gate)
- Sources retrieved: admin_library_holds.txt, housing_aldridge_hall.txt, housing_calder_annexe_noise.txt, study_group_rooms.txt, transit_walking.txt

```
I don't have enough information to answer your question from the provided documents.
```

### How far is the university clinic from the library on campus? — run 3

- Best distance: 0.5078 (passed the gate)
- Sources retrieved: admin_library_holds.txt, housing_aldridge_hall.txt, housing_calder_annexe_noise.txt, study_group_rooms.txt, transit_walking.txt

```
I do not have enough information to answer this question from the provided documents.
```

### When is it a good time go the university dining hall on a Tuesday evening? — run 1

- Best distance: 0.4033 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt

```
Based on the provided documents, I do not have enough information to answer when it is a good time to go to the university dining hall on a Tuesday evening.
```

### When is it a good time go the university dining hall on a Tuesday evening? — run 2

- Best distance: 0.4033 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt

```
Based on the provided documents, Halden Hall is open on weekdays (which includes Tuesdays) until 7:00pm (`dining_halden_hall.txt`). Pellew Dining Hall is open daily from 7:00am to 8:00pm (`dining_pellew_dining_hall.txt`).
```

### When is it a good time go the university dining hall on a Tuesday evening? — run 3

- Best distance: 0.4033 (passed the gate)
- Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt

```
Based on the provided documents, I do not have enough information to answer when it is a good time to go to the university dining hall on a Tuesday evening.
```
