use m101
db.zips.aggregate([
	{$group:
		{
			_id:"$state", 
			"population":{$sum:"$pop"}
		}
	}
])