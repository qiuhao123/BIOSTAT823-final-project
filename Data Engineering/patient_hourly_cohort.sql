CREATE TABLE mp_hourly_cohort as
select
  co.subject_id, co.hadm_id, co.icustay_id
  ,date_diff('hour',intime,outtime) as hr
from mp_cohort co
where co.excluded = 0
order by co.subject_id, co.hadm_id, co.icustay_id;