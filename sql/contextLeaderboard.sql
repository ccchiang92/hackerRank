select h.hacker_id, h.name, sum(s.max_score)as sum_score from
Hackers as h
join (select hacker_id, max(score) as max_score from Submissions 
      group by challenge_id, hacker_id) s
on h.hacker_id = s.hacker_id
group by h.hacker_id, h.name
having sum_score >0 
order by sum_score desc, h.hacker_id;