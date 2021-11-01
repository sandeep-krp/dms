import React from 'react';
import axios from 'axios';
import {Table} from 'antd';
class Migrations extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            migrations: [],
            loading: true
        }
    }

    async getMigrationsData() {
        try {
            const res = await axios.get('http://localhost:8080/api/v1/migrationjob')
            this.setState({ loading: false, migrations: res.data })
        } catch {
            console.error("Could not get migrations")
        }
    }

    componentDidMount() {
        this.getMigrationsData()
    }

    render() {
        const columns = [
            {
                title: 'ID',
                key: 'id',
                dataIndex: 'id'
            },
            {
                title: 'Name',
                key: 'name',
                dataIndex: 'name'
            },
            {
                title: 'Type',
                key: 'source_id',
                dataIndex: 'source_id'
            },
            {
                title: 'Type',
                key: 'target_id',
                dataIndex: 'target_id'
            },
            {
                title: 'Schema',
                key: 'conf_blob',
                dataIndex: 'conf_blob',
                render: d => JSON.stringify(d)
            }
        ]
        return (<div style={{ height: 400, width: '70%' }}>
                <Table
                    dataSource = {this.state.migrations}
                    columns = {columns}
                />
                </div>
        );
    }
}

export default Migrations;