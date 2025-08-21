function query_filter( $admin_query ) {
	global $pagenow;
	$post_type = (isset($_GET['post_type'])) ? $_GET['post_type'] : 'post';

	if ( $post_type == 'post' && in_array( $pagenow, array('edit.php', 'upload.php') && ( ! empty( $_GET['event_date_from'] ) || ! empty( $_GET['event_date_to'] ) ))) {
		$admin_query->set(
			'date_query', // date_query appeared in WordPress 3.7!
			array(
				'after' => sanitize_text_field( $_GET['event_date_from'] ),
				'before' => sanitize_text_field( $_GET['event_date_to'] ),
				'inclusive' => true, // include the selected days as well
				'column' => 'post_date' // 'post_modified', 'post_date_gmt', 'post_modified_gmt'
			)
		);
	}

	return $admin_query;
}