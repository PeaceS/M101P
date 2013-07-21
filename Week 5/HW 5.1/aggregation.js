use blog
db.posts.aggregate([
	{$group:
		{
			_id:"$author",
			num_comment:{$sum:1}
		}
	}
])