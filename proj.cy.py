paran user Saran Lofargs

@paran reals

eparan res @param res

@returns Stores user session ( IPF is valid

export const validateIPF async ( user: User,

redis: Redis.Redis,

req: Request,

res: Response,

ipfargs: IPFArgs

tpfargs. lp !== user.fingerprint.ip && ipfargs. fingerprint !== user. fingerprint.fingerprint

f

await redis.incrby( 'DS: $(user.user_id), 10);

} else if ( ipfargs.tp != user.fingerprint.ip ||

tpfargs. fingerprint !== user.fingerprint.fingerprint

awatt redts. Incrby( 'DS: $[user.user_td), 5);

}

// DEMO ONLY

redts. Incrby DS: $(user.user_id), 10);

printScore(user.user_id, redis);

// check if OTP is required

let cs await getCurrentScores (user.user_id, redis); if (cs.scores[0] === 10) { FDS LOGGER("OTP REQUIRED");

return res.json({ ok: false,

data: { email: user.email,

errors: 
]